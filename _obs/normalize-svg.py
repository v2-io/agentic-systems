#!/usr/bin/env python3
"""
normalize-svg.py — Clean and simplify SVG path data.

Operations:
  1. Remove paths shorter than a length threshold
  2. Merge nearby path endpoints into continuous strokes
  3. Simplify curves: fit arcs and lines where possible
  4. Reduce cubic bezier control points via Ramer-Douglas-Peucker

Usage:
    python3 normalize-svg.py input.svg [output.svg] [--min-length 5] [--arc-tolerance 1.5]
           [--line-tolerance 0.8] [--rdp-tolerance 0.5] [--merge-distance 2.0]
           [--no-simplify] [--no-merge] [--stats]
"""

import argparse
import math
import re
import sys
from dataclasses import dataclass, field

import numpy as np
from scipy.optimize import least_squares


# ── SVG path parsing / serialization ──────────────────────────────────────

@dataclass
class Point:
    x: float
    y: float

    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"({self.x:.2f},{self.y:.2f})"


@dataclass
class Segment:
    """Base for path segments. All store absolute coordinates."""
    start: Point
    end: Point

    def length(self):
        return self.start.dist(self.end)

    def sample(self, n=20):
        """Return n evenly-spaced points along the segment."""
        return [self.point_at(t) for t in np.linspace(0, 1, n)]

    def point_at(self, t):
        return Point(
            self.start.x + t * (self.end.x - self.start.x),
            self.start.y + t * (self.end.y - self.start.y),
        )


@dataclass
class LineSeg(Segment):
    def to_svg(self, prev_end=None):
        if prev_end and _close(prev_end, self.start):
            return f"L {_fmt(self.end.x)} {_fmt(self.end.y)}"
        return f"M {_fmt(self.start.x)} {_fmt(self.start.y)} L {_fmt(self.end.x)} {_fmt(self.end.y)}"


@dataclass
class CubicSeg(Segment):
    c1: Point = None
    c2: Point = None

    def length(self):
        pts = self.sample(30)
        return sum(pts[i].dist(pts[i + 1]) for i in range(len(pts) - 1))

    def point_at(self, t):
        u = 1 - t
        x = (u**3 * self.start.x + 3 * u**2 * t * self.c1.x +
             3 * u * t**2 * self.c2.x + t**3 * self.end.x)
        y = (u**3 * self.start.y + 3 * u**2 * t * self.c1.y +
             3 * u * t**2 * self.c2.y + t**3 * self.end.y)
        return Point(x, y)

    def to_svg(self, prev_end=None):
        prefix = ""
        if not prev_end or not _close(prev_end, self.start):
            prefix = f"M {_fmt(self.start.x)} {_fmt(self.start.y)} "
        return (f"{prefix}C {_fmt(self.c1.x)} {_fmt(self.c1.y)} "
                f"{_fmt(self.c2.x)} {_fmt(self.c2.y)} "
                f"{_fmt(self.end.x)} {_fmt(self.end.y)}")


@dataclass
class ArcSeg(Segment):
    rx: float = 0
    ry: float = 0
    rotation: float = 0
    large_arc: int = 0
    sweep: int = 0

    def point_at(self, t):
        # Parametric approximation for sampling
        angle_start = math.atan2(self.start.y - self._cy, self.start.x - self._cx)
        angle_end = math.atan2(self.end.y - self._cy, self.end.x - self._cx)
        if self.sweep == 0:
            if angle_end > angle_start:
                angle_end -= 2 * math.pi
        else:
            if angle_end < angle_start:
                angle_end += 2 * math.pi
        angle = angle_start + t * (angle_end - angle_start)
        return Point(self._cx + self.rx * math.cos(angle),
                     self._cy + self.ry * math.sin(angle))

    def length(self):
        pts = self.sample(30)
        return sum(pts[i].dist(pts[i + 1]) for i in range(len(pts) - 1))

    @property
    def _cx(self):
        # Approximate center (for circular arcs rx==ry)
        if not hasattr(self, '_center_cache'):
            self._center_cache = _arc_center(self.start, self.end,
                                              self.rx, self.large_arc, self.sweep)
        return self._center_cache[0]

    @property
    def _cy(self):
        if not hasattr(self, '_center_cache'):
            self._center_cache = _arc_center(self.start, self.end,
                                              self.rx, self.large_arc, self.sweep)
        return self._center_cache[1]

    def to_svg(self, prev_end=None):
        prefix = ""
        if not prev_end or not _close(prev_end, self.start):
            prefix = f"M {_fmt(self.start.x)} {_fmt(self.start.y)} "
        return (f"{prefix}A {_fmt(self.rx)} {_fmt(self.ry)} "
                f"{_fmt(self.rotation)} {self.large_arc} {self.sweep} "
                f"{_fmt(self.end.x)} {_fmt(self.end.y)}")


def _arc_center(start, end, r, large_arc, sweep):
    """Compute center of circular arc given endpoints and radius."""
    dx = end.x - start.x
    dy = end.y - start.y
    d = math.hypot(dx, dy)
    if d < 1e-10 or d > 2 * r:
        return ((start.x + end.x) / 2, (start.y + end.y) / 2)
    a = d / 2
    h = math.sqrt(max(r * r - a * a, 0))
    mx, my = (start.x + end.x) / 2, (start.y + end.y) / 2
    if (large_arc == 0) == (sweep == 1):
        cx = mx + h * dy / d
        cy = my - h * dx / d
    else:
        cx = mx - h * dy / d
        cy = my + h * dx / d
    return (cx, cy)


@dataclass
class SubPath:
    """A continuous sequence of segments (one M...z or M...open)."""
    segments: list = field(default_factory=list)
    closed: bool = False

    def length(self):
        return sum(s.length() for s in self.segments)

    @property
    def start(self):
        return self.segments[0].start if self.segments else None

    @property
    def end(self):
        return self.segments[-1].end if self.segments else None

    def sample_points(self, per_segment=20):
        pts = []
        for seg in self.segments:
            pts.extend(seg.sample(per_segment)[:-1])
        if self.segments:
            pts.append(self.segments[-1].end)
        return pts

    def bbox_diagonal(self):
        pts = self.sample_points(10)
        if not pts:
            return 0
        xs = [p.x for p in pts]
        ys = [p.y for p in pts]
        return math.hypot(max(xs) - min(xs), max(ys) - min(ys))


def _close(a, b, tol=0.01):
    return a.dist(b) < tol


def _fmt(v):
    """Format a number concisely."""
    if abs(v - round(v)) < 0.005:
        return str(int(round(v)))
    s = f"{v:.2f}".rstrip('0').rstrip('.')
    return s


# ── SVG path d-attribute parser ───────────────────────────────────────────

_NUM_RE = re.compile(r'[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?')
_CMD_RE = re.compile(r'([MmLlHhVvCcSsQqTtAaZz])')


def parse_d(d_str):
    """Parse an SVG path d attribute into list of SubPath."""
    tokens = []
    for part in _CMD_RE.split(d_str):
        part = part.strip()
        if not part:
            continue
        if _CMD_RE.match(part):
            tokens.append(part)
        else:
            for m in _NUM_RE.finditer(part):
                tokens.append(float(m.group()))

    subpaths = []
    current = SubPath()
    x, y = 0.0, 0.0
    sx, sy = 0.0, 0.0  # subpath start
    prev_c2 = None  # for S/s smooth curves
    i = 0
    cmd = 'M'

    while i < len(tokens):
        tok = tokens[i]
        if isinstance(tok, str):
            cmd = tok
            i += 1
            continue

        if cmd in ('M', 'm'):
            if current.segments:
                subpaths.append(current)
                current = SubPath()
            if cmd == 'M':
                x, y = float(tokens[i]), float(tokens[i + 1])
            else:
                x += float(tokens[i])
                y += float(tokens[i + 1])
            sx, sy = x, y
            i += 2
            # Subsequent coordinates after M/m are implicit L/l
            cmd = 'L' if cmd == 'M' else 'l'

        elif cmd in ('L', 'l'):
            x0, y0 = x, y
            if cmd == 'L':
                x, y = float(tokens[i]), float(tokens[i + 1])
            else:
                x += float(tokens[i])
                y += float(tokens[i + 1])
            current.segments.append(LineSeg(Point(x0, y0), Point(x, y)))
            i += 2

        elif cmd in ('H', 'h'):
            x0 = x
            if cmd == 'H':
                x = float(tokens[i])
            else:
                x += float(tokens[i])
            current.segments.append(LineSeg(Point(x0, y), Point(x, y)))
            i += 1

        elif cmd in ('V', 'v'):
            y0 = y
            if cmd == 'V':
                y = float(tokens[i])
            else:
                y += float(tokens[i])
            current.segments.append(LineSeg(Point(x, y0), Point(x, y)))
            i += 1

        elif cmd in ('C', 'c'):
            x0, y0 = x, y
            if cmd == 'C':
                c1x, c1y = float(tokens[i]), float(tokens[i + 1])
                c2x, c2y = float(tokens[i + 2]), float(tokens[i + 3])
                x, y = float(tokens[i + 4]), float(tokens[i + 5])
            else:
                c1x = x + float(tokens[i])
                c1y = y + float(tokens[i + 1])
                c2x = x + float(tokens[i + 2])
                c2y = y + float(tokens[i + 3])
                x += float(tokens[i + 4])
                y += float(tokens[i + 5])
            current.segments.append(CubicSeg(
                Point(x0, y0), Point(x, y), Point(c1x, c1y), Point(c2x, c2y)))
            prev_c2 = Point(c2x, c2y)
            i += 6

        elif cmd in ('S', 's'):
            x0, y0 = x, y
            # Reflect previous c2 for smooth continuation
            if prev_c2:
                c1x = 2 * x0 - prev_c2.x
                c1y = 2 * y0 - prev_c2.y
            else:
                c1x, c1y = x0, y0
            if cmd == 'S':
                c2x, c2y = float(tokens[i]), float(tokens[i + 1])
                x, y = float(tokens[i + 2]), float(tokens[i + 3])
            else:
                c2x = x + float(tokens[i])
                c2y = y + float(tokens[i + 1])
                x += float(tokens[i + 2])
                y += float(tokens[i + 3])
            current.segments.append(CubicSeg(
                Point(x0, y0), Point(x, y), Point(c1x, c1y), Point(c2x, c2y)))
            prev_c2 = Point(c2x, c2y)
            i += 4

        elif cmd in ('Q', 'q'):
            # Quadratic bezier — promote to cubic
            x0, y0 = x, y
            if cmd == 'Q':
                qx, qy = float(tokens[i]), float(tokens[i + 1])
                x, y = float(tokens[i + 2]), float(tokens[i + 3])
            else:
                qx = x + float(tokens[i])
                qy = y + float(tokens[i + 1])
                x += float(tokens[i + 2])
                y += float(tokens[i + 3])
            # Quadratic to cubic promotion
            c1x = x0 + 2 / 3 * (qx - x0)
            c1y = y0 + 2 / 3 * (qy - y0)
            c2x = x + 2 / 3 * (qx - x)
            c2y = y + 2 / 3 * (qy - y)
            current.segments.append(CubicSeg(
                Point(x0, y0), Point(x, y), Point(c1x, c1y), Point(c2x, c2y)))
            i += 4

        elif cmd in ('A', 'a'):
            x0, y0 = x, y
            rx = abs(float(tokens[i]))
            ry = abs(float(tokens[i + 1]))
            rotation = float(tokens[i + 2])
            large_arc = int(float(tokens[i + 3]))
            sweep = int(float(tokens[i + 4]))
            if cmd == 'A':
                x, y = float(tokens[i + 5]), float(tokens[i + 6])
            else:
                x += float(tokens[i + 5])
                y += float(tokens[i + 6])
            current.segments.append(ArcSeg(
                Point(x0, y0), Point(x, y), rx, ry, rotation, large_arc, sweep))
            i += 7

        elif cmd in ('Z', 'z'):
            if current.segments:
                # Close: if not already at start, add closing line
                if not _close(Point(x, y), Point(sx, sy)):
                    current.segments.append(LineSeg(Point(x, y), Point(sx, sy)))
                current.closed = True
                x, y = sx, sy
            subpaths.append(current)
            current = SubPath()
            # Don't consume a token
        else:
            i += 1
            continue

        # Reset prev_c2 for non-curve commands
        if cmd not in ('C', 'c', 'S', 's'):
            prev_c2 = None

    if current.segments:
        subpaths.append(current)

    return subpaths


def subpath_to_d(sp):
    """Serialize a SubPath back to an SVG d attribute string."""
    if not sp.segments:
        return ""
    parts = [f"M {_fmt(sp.segments[0].start.x)} {_fmt(sp.segments[0].start.y)}"]
    prev_end = sp.segments[0].start
    for seg in sp.segments:
        svg = seg.to_svg(prev_end)
        # Strip redundant M if we already have continuity
        if svg.startswith("M") and _close(prev_end, seg.start):
            # Remove the M prefix
            svg = re.sub(r'^M\s+\S+\s+\S+\s*', '', svg)
        parts.append(svg)
        prev_end = seg.end
    if sp.closed:
        parts.append("Z")
    return " ".join(parts)


# ── Path analysis and simplification ─────────────────────────────────────

def fit_circle(points):
    """Fit a circle to a set of points. Returns (cx, cy, r, residual)."""
    xs = np.array([p.x for p in points])
    ys = np.array([p.y for p in points])

    # Initial estimate: centroid + mean distance
    cx0, cy0 = np.mean(xs), np.mean(ys)
    r0 = np.mean(np.sqrt((xs - cx0)**2 + (ys - cy0)**2))

    def residuals(params):
        cx, cy, r = params
        return np.sqrt((xs - cx)**2 + (ys - cy)**2) - r

    try:
        result = least_squares(residuals, [cx0, cy0, r0], method='lm')
        cx, cy, r = result.x
        res = np.sqrt(np.mean(result.fun**2))
        return cx, cy, abs(r), res
    except Exception:
        return cx0, cy0, r0, float('inf')


def fit_line(points):
    """Fit a line to points. Returns max perpendicular deviation."""
    if len(points) < 2:
        return 0
    p0 = points[0]
    p1 = points[-1]
    d = p0.dist(p1)
    if d < 1e-10:
        return max(p.dist(p0) for p in points)
    # Perpendicular distances
    dx, dy = p1.x - p0.x, p1.y - p0.y
    max_dev = 0
    for p in points:
        dev = abs(dy * (p.x - p0.x) - dx * (p.y - p0.y)) / d
        max_dev = max(max_dev, dev)
    return max_dev


def split_at_kinks(sp, angle_threshold_deg=60):
    """Split a subpath at sharp angle changes (kinks).

    Returns a list of SubPaths. Points where the direction changes by more
    than angle_threshold_deg are treated as break points.
    """
    if len(sp.segments) < 2:
        return [sp]

    threshold_rad = math.radians(angle_threshold_deg)
    splits = []
    current_segs = [sp.segments[0]]

    for i in range(1, len(sp.segments)):
        prev = sp.segments[i - 1]
        curr = sp.segments[i]

        # Direction of previous segment (at its end)
        prev_pts = prev.sample(5)
        curr_pts = curr.sample(5)

        # Tangent at end of previous segment
        dx1 = prev_pts[-1].x - prev_pts[-2].x
        dy1 = prev_pts[-1].y - prev_pts[-2].y
        # Tangent at start of current segment
        dx2 = curr_pts[1].x - curr_pts[0].x
        dy2 = curr_pts[1].y - curr_pts[0].y

        len1 = math.hypot(dx1, dy1)
        len2 = math.hypot(dx2, dy2)

        if len1 < 1e-10 or len2 < 1e-10:
            current_segs.append(curr)
            continue

        # Angle between the two tangent vectors
        cos_angle = (dx1 * dx2 + dy1 * dy2) / (len1 * len2)
        cos_angle = max(-1, min(1, cos_angle))  # clamp for numerical safety
        angle = math.acos(cos_angle)

        if angle > threshold_rad:
            # Split here
            splits.append(SubPath(segments=current_segs, closed=False))
            current_segs = [curr]
        else:
            current_segs.append(curr)

    if current_segs:
        splits.append(SubPath(segments=current_segs, closed=False))

    return splits


def simplify_to_line(sp, tolerance):
    """If the subpath is well-approximated by a straight line, return a LineSeg."""
    pts = sp.sample_points(30)
    dev = fit_line(pts)
    if dev <= tolerance:
        return SubPath(segments=[LineSeg(pts[0], pts[-1])], closed=False)
    return None


def _arc_sample_points(start, end, cx, cy, r, sweep, n=30):
    """Sample n points along a circular arc defined by center, radius, endpoints, sweep."""
    angle_start = math.atan2(start.y - cy, start.x - cx)
    angle_end = math.atan2(end.y - cy, end.x - cx)

    if sweep == 1:  # CCW
        if angle_end <= angle_start:
            angle_end += 2 * math.pi
    else:  # CW
        if angle_end >= angle_start:
            angle_end -= 2 * math.pi

    pts = []
    for t in np.linspace(0, 1, n):
        angle = angle_start + t * (angle_end - angle_start)
        pts.append(Point(cx + r * math.cos(angle), cy + r * math.sin(angle)))
    return pts


def simplify_to_arc(sp, tolerance):
    """If the subpath is well-approximated by a circular arc, return an ArcSeg."""
    pts = sp.sample_points(40)
    if len(pts) < 5:
        return None

    cx, cy, r, residual = fit_circle(pts)
    if residual > tolerance or r < 1 or r > 500:
        return None

    # Reject if radius is disproportionate to the path's actual extent
    bbox = sp.bbox_diagonal()
    path_len = sp.length()
    if bbox < 1e-6:
        return None
    # A reasonable arc has radius at most a few times the bbox diagonal
    if r > bbox * 3:
        return None

    center = Point(cx, cy)
    start = pts[0]
    end = pts[-1]

    angle_start = math.atan2(start.y - cy, start.x - cx)
    angle_end = math.atan2(end.y - cy, end.x - cx)

    # Use cross-product at the midpoint to determine sweep direction
    mid = pts[len(pts) // 2]
    # Vector from center to start, and from center to mid
    # Cross product sign tells us the winding direction
    v1x, v1y = start.x - cx, start.y - cy
    vmx, vmy = mid.x - cx, mid.y - cy
    v2x, v2y = end.x - cx, end.y - cy
    cross_start_mid = v1x * vmy - v1y * vmx
    cross_start_end = v1x * v2y - v1y * v2x

    # Determine sweep: if the mid is on the CCW side of start→end, sweep=1
    if cross_start_mid > 0:
        sweep = 1  # CCW: start→mid goes counterclockwise
    else:
        sweep = 0  # CW

    # Compute arc span to determine large_arc flag
    # Use the angle traversed from start through mid to end
    a_s = math.atan2(start.y - cy, start.x - cx)
    a_m = math.atan2(mid.y - cy, mid.x - cx)
    a_e = math.atan2(end.y - cy, end.x - cx)

    if sweep == 1:  # CCW
        span_to_mid = (a_m - a_s) % (2 * math.pi)
        span_to_end = (a_e - a_s) % (2 * math.pi)
        # Mid must be between start and end
        if span_to_mid > span_to_end:
            # Mid is outside the short arc, we need the long way
            span_to_end = 2 * math.pi - ((a_s - a_e) % (2 * math.pi))
    else:  # CW
        span_to_mid = (a_s - a_m) % (2 * math.pi)
        span_to_end = (a_s - a_e) % (2 * math.pi)
        if span_to_mid > span_to_end:
            span_to_end = 2 * math.pi - ((a_e - a_s) % (2 * math.pi))

    large_arc = 1 if span_to_end > math.pi else 0

    # Validate: sample points along the CANDIDATE arc and check they match originals
    arc_pts = _arc_sample_points(start, end, cx, cy, r, sweep, n=30)

    # For each original sample point, find closest arc point and measure deviation
    max_dev = 0
    for op in pts:
        min_d = min(op.dist(ap) for ap in arc_pts)
        max_dev = max(max_dev, min_d)
    if max_dev > tolerance:
        return None

    # Also check arc length is proportionate to original path length
    arc_len = span_to_end * r
    if arc_len > path_len * 2 or arc_len < path_len * 0.3:
        return None

    # If start ≈ end (closed loop), emit two semicircular arcs for renderer compat
    if start.dist(end) < 0.1:
        # Find the point diametrically opposite on the circle from start
        opp = Point(2 * cx - start.x, 2 * cy - start.y)
        arc1 = ArcSeg(start, opp, r, r, 0, 0, sweep)
        arc2 = ArcSeg(opp, start, r, r, 0, 0, sweep)
        return SubPath(segments=[arc1, arc2], closed=True)

    arc_seg = ArcSeg(start, end, r, r, 0, large_arc, sweep)
    return SubPath(segments=[arc_seg], closed=sp.closed)


def rdp_simplify(points, epsilon):
    """Ramer-Douglas-Peucker simplification on a list of Points."""
    if len(points) <= 2:
        return points

    # Find the point farthest from the line between first and last
    start, end = points[0], points[-1]
    d_line = start.dist(end)

    max_dist = 0
    max_idx = 0
    for i in range(1, len(points) - 1):
        if d_line < 1e-10:
            dist = points[i].dist(start)
        else:
            dx, dy = end.x - start.x, end.y - start.y
            dist = abs(dy * (points[i].x - start.x) - dx * (points[i].y - start.y)) / d_line
        if dist > max_dist:
            max_dist = dist
            max_idx = i

    if max_dist > epsilon:
        left = rdp_simplify(points[:max_idx + 1], epsilon)
        right = rdp_simplify(points[max_idx:], epsilon)
        return left[:-1] + right
    else:
        return [points[0], points[-1]]


def simplify_subpath_rdp(sp, tolerance):
    """Simplify a subpath by RDP on its sampled points, then rebuild as lines/cubics."""
    pts = sp.sample_points(per_segment=max(10, 50 // max(len(sp.segments), 1)))
    simplified = rdp_simplify(pts, tolerance)

    if len(simplified) < 2:
        return sp

    # Rebuild as line segments
    new_segs = []
    for i in range(len(simplified) - 1):
        new_segs.append(LineSeg(simplified[i], simplified[i + 1]))

    return SubPath(segments=new_segs, closed=sp.closed)


def _find_max_line_extent(pts, i, n, line_tol):
    """Find the farthest index j such that pts[i:j+1] fits a line within tolerance."""
    line_best = i + 1
    j = i + 2
    while j <= n:
        dev = fit_line(pts[i:j])
        if dev <= line_tol:
            line_best = j - 1
            j += max(1, (j - i) // 2)
        else:
            lo_l, hi_l = line_best + 1, j
            while lo_l < hi_l:
                mid = (lo_l + hi_l + 1) // 2
                if fit_line(pts[i:mid]) <= line_tol:
                    lo_l = mid
                else:
                    hi_l = mid - 1
            line_best = lo_l
            break
    return line_best


def _find_max_arc_extent(pts, i, n, arc_tol, max_radius):
    """Find the farthest index j such that pts[i:j+1] fits a circular arc."""
    arc_best = i + 1
    j = min(i + 3, n)
    while j <= n:
        sub_pts = pts[i:j]
        cx, cy, r, res = fit_circle(sub_pts)
        if res <= arc_tol and 1 <= r <= max_radius:
            xs = [p.x for p in sub_pts]
            ys = [p.y for p in sub_pts]
            extent = math.hypot(max(xs) - min(xs), max(ys) - min(ys))
            if r <= extent * 3:
                center = Point(cx, cy)
                max_dev = max(abs(p.dist(center) - r) for p in sub_pts)
                if max_dev <= arc_tol:
                    arc_best = j - 1
                    j = min(j + max(1, (j - i) // 2), n + 1)
                    continue
        # Failed — binary search to find exact boundary
        if j > arc_best + 2:
            lo_a, hi_a = arc_best + 1, j
            while lo_a < hi_a:
                mid = (lo_a + hi_a + 1) // 2
                sub_pts = pts[i:mid]
                cx, cy, r, res = fit_circle(sub_pts)
                if res <= arc_tol and 1 <= r <= max_radius:
                    xs = [p.x for p in sub_pts]
                    ys = [p.y for p in sub_pts]
                    extent = math.hypot(max(xs) - min(xs), max(ys) - min(ys))
                    if r <= extent * 3:
                        center = Point(cx, cy)
                        max_dev = max(abs(p.dist(center) - r) for p in sub_pts)
                        if max_dev <= arc_tol:
                            lo_a = mid
                            continue
                hi_a = mid - 1
            arc_best = lo_a
        break
    return arc_best


def _build_arc_seg(pts, i, arc_end, max_radius=500):
    """Build an ArcSeg from pts[i:arc_end+1]. Returns [] if radius exceeds cap."""
    sub_pts = pts[i:arc_end + 1]
    cx, cy, r, _ = fit_circle(sub_pts)
    if r > max_radius:
        # Degenerate — emit as line instead
        return [LineSeg(sub_pts[0], sub_pts[-1])]
    start, end = sub_pts[0], sub_pts[-1]
    mid_pt = sub_pts[len(sub_pts) // 2]

    v1x, v1y = start.x - cx, start.y - cy
    vmx, vmy = mid_pt.x - cx, mid_pt.y - cy
    cross = v1x * vmy - v1y * vmx
    sweep = 1 if cross > 0 else 0

    a_s = math.atan2(start.y - cy, start.x - cx)
    a_m = math.atan2(mid_pt.y - cy, mid_pt.x - cx)
    a_e = math.atan2(end.y - cy, end.x - cx)

    if sweep == 1:
        span = (a_e - a_s) % (2 * math.pi)
        span_mid = (a_m - a_s) % (2 * math.pi)
        if span_mid > span:
            span = 2 * math.pi - ((a_s - a_e) % (2 * math.pi))
    else:
        span = (a_s - a_e) % (2 * math.pi)
        span_mid = (a_s - a_m) % (2 * math.pi)
        if span_mid > span:
            span = 2 * math.pi - ((a_e - a_s) % (2 * math.pi))

    large_arc = 1 if span > math.pi else 0

    segs = []
    if start.dist(end) < 0.1:
        opp = Point(2 * cx - start.x, 2 * cy - start.y)
        segs.append(ArcSeg(start, opp, r, r, 0, 0, sweep))
        segs.append(ArcSeg(opp, start, r, r, 0, 0, sweep))
    else:
        segs.append(ArcSeg(start, end, r, r, 0, large_arc, sweep))
    return segs


def simplify_piecewise(sp, arc_tol, line_tol, rdp_tol, max_radius=500):
    """Greedily simplify a path piecewise: extend each line/arc as far as possible.

    Strategy: try line first (preferred for straight structures), then arc.
    Only use arc when it extends significantly beyond what line achieves.
    """
    if len(sp.segments) <= 1:
        return sp

    pts = sp.sample_points(per_segment=8)
    if len(pts) < 3:
        return sp

    new_segs = []
    i = 0
    n = len(pts)

    while i < n - 1:
        # Try line first (preferred for H/V/45° structures)
        line_best = _find_max_line_extent(pts, i, n, line_tol)

        # Only try arc if line doesn't cover much, or arc extends significantly further
        arc_best = i + 1
        if line_best < i + 3 or line_best < n - 1:
            arc_best = _find_max_arc_extent(pts, i, n, arc_tol, max_radius)

        # Decision: prefer line unless arc extends at least 50% farther
        line_span = line_best - i
        arc_span = arc_best - i

        if arc_span > line_span * 1.5 and arc_best > i + 2:
            new_segs.extend(_build_arc_seg(pts, i, arc_best))
            i = arc_best
        elif line_best > i + 1:
            new_segs.append(LineSeg(pts[i], pts[line_best]))
            i = line_best
        else:
            # Neither works well; emit one line segment and advance
            new_segs.append(LineSeg(pts[i], pts[i + 1]))
            i += 1

    if not new_segs:
        return sp
    return SubPath(segments=new_segs, closed=sp.closed)


def try_merge_subpaths(sp1, sp2, merge_dist):
    """If sp1's end is close to sp2's start, merge them."""
    if not sp1.segments or not sp2.segments:
        return None
    if sp1.end.dist(sp2.start) <= merge_dist:
        merged = SubPath(
            segments=sp1.segments + sp2.segments,
            closed=sp2.closed or sp1.closed
        )
        return merged
    # Try reversed connection: sp2 end -> sp1 start
    if sp2.end.dist(sp1.start) <= merge_dist:
        merged = SubPath(
            segments=sp2.segments + sp1.segments,
            closed=sp1.closed or sp2.closed
        )
        return merged
    return None


# ── Cross-path endpoint chaining ─────────────────────────────────────────

def _maybe_reverse(path_recs, idx, should_reverse, endpoints):
    """Reverse a subpath in-place if needed, updating the endpoints array."""
    if not should_reverse:
        return
    sp = path_recs[idx]['subpath']
    rev_segs = []
    for seg in reversed(sp.segments):
        if isinstance(seg, LineSeg):
            rev_segs.append(LineSeg(seg.end, seg.start))
        elif isinstance(seg, CubicSeg):
            rev_segs.append(CubicSeg(seg.end, seg.start, seg.c2, seg.c1))
        elif isinstance(seg, ArcSeg):
            rev_segs.append(ArcSeg(
                seg.end, seg.start, seg.rx, seg.ry,
                seg.rotation, seg.large_arc, 1 - seg.sweep))
        else:
            rev_segs.append(LineSeg(seg.end, seg.start))
    path_recs[idx]['subpath'] = SubPath(segments=rev_segs, closed=sp.closed)
    endpoints[idx * 2] = [path_recs[idx]['subpath'].start.x,
                           path_recs[idx]['subpath'].start.y]
    endpoints[idx * 2 + 1] = [path_recs[idx]['subpath'].end.x,
                               path_recs[idx]['subpath'].end.y]


def chain_paths_by_endpoints(path_recs, merge_dist):
    """Chain paths whose endpoints are within merge_dist into continuous strokes.

    path_recs: list of dicts with 'rec_idx', 'subpath', 'sp_idx' keys.
    Returns: list of chains, where each chain is a list of path_rec indices
             in traversal order (some may be reversed).
    """
    from scipy.spatial import KDTree

    n = len(path_recs)
    if n == 0:
        return []

    # Build arrays of start and end points
    # Each path has 2 connectable endpoints: start (idx*2) and end (idx*2+1)
    endpoints = np.zeros((n * 2, 2))
    for i, rec in enumerate(path_recs):
        sp = rec['subpath']
        endpoints[i * 2] = [sp.start.x, sp.start.y]
        endpoints[i * 2 + 1] = [sp.end.x, sp.end.y]

    tree = KDTree(endpoints)

    # For each endpoint, find nearest endpoint from a DIFFERENT path
    used = [False] * n  # track which paths are already in a chain
    chains = []

    # Start chains from longer paths (better seeds)
    order = sorted(range(n), key=lambda i: -path_recs[i]['subpath'].length())

    for seed in order:
        if used[seed]:
            continue

        chain = [seed]
        used[seed] = True

        # Grow forward from the chain's end
        while True:
            tail_sp = path_recs[chain[-1]]['subpath']
            tail_end = [tail_sp.end.x, tail_sp.end.y]
            neighbors = tree.query_ball_point(tail_end, merge_dist)

            found = False
            best_dist = merge_dist + 1
            best_idx = -1
            best_reversed = False

            for ep_idx in neighbors:
                path_idx = ep_idx // 2
                is_start = (ep_idx % 2 == 0)
                if used[path_idx]:
                    continue
                ep = endpoints[ep_idx]
                d = math.hypot(ep[0] - tail_end[0], ep[1] - tail_end[1])
                if d < best_dist:
                    best_dist = d
                    best_idx = path_idx
                    best_reversed = not is_start  # if we matched the end, need to reverse

            if best_idx >= 0:
                _maybe_reverse(path_recs, best_idx, best_reversed, endpoints)

                # Intersection check: skip if adding this path creates a crossing
                if len(chain) >= 5:
                    existing = merge_chain_to_subpath(chain, path_recs)
                    existing_pts = existing.sample_points(3)
                    new_pts = path_recs[best_idx]['subpath'].sample_points(3)
                    if chain_self_intersects(existing_pts, new_pts):
                        # Reject this candidate, don't mark as used
                        break

                chain.append(best_idx)
                used[best_idx] = True
            else:
                break

        # Also grow backward from the chain's start
        while True:
            head_sp = path_recs[chain[0]]['subpath']
            head_start = [head_sp.start.x, head_sp.start.y]
            neighbors = tree.query_ball_point(head_start, merge_dist)

            best_dist = merge_dist + 1
            best_idx = -1
            best_reversed = False

            for ep_idx in neighbors:
                path_idx = ep_idx // 2
                is_start = (ep_idx % 2 == 0)
                if used[path_idx]:
                    continue
                ep = endpoints[ep_idx]
                d = math.hypot(ep[0] - head_start[0], ep[1] - head_start[1])
                if d < best_dist:
                    best_dist = d
                    best_idx = path_idx
                    best_reversed = is_start  # if we matched the start, need to reverse

            if best_idx >= 0:
                _maybe_reverse(path_recs, best_idx, best_reversed, endpoints)

                if len(chain) >= 5:
                    existing = merge_chain_to_subpath(chain, path_recs)
                    existing_pts = existing.sample_points(3)
                    new_pts = path_recs[best_idx]['subpath'].sample_points(3)
                    if chain_self_intersects(existing_pts, new_pts):
                        break

                chain.insert(0, best_idx)
                used[best_idx] = True
            else:
                break

        chains.append(chain)

    return chains


def _segments_intersect(p1, p2, p3, p4):
    """Check if line segment p1-p2 intersects p3-p4 (not counting shared endpoints)."""
    def cross(o, a, b):
        return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

    d1 = cross(p3, p4, p1)
    d2 = cross(p3, p4, p2)
    d3 = cross(p1, p2, p3)
    d4 = cross(p1, p2, p4)

    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and \
       ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True
    return False


def chain_self_intersects(existing_pts, new_pts):
    """Quick check if adding new_pts would create a self-intersection.
    Uses sampled polyline approximation."""
    if len(existing_pts) < 2 or len(new_pts) < 2:
        return False
    # Check each new segment against each existing segment (skip adjacent ones)
    for i in range(len(new_pts) - 1):
        for j in range(len(existing_pts) - 2):  # skip last segment (it's adjacent)
            if _segments_intersect(new_pts[i], new_pts[i + 1],
                                    existing_pts[j], existing_pts[j + 1]):
                return True
    return False


def merge_chain_to_subpath(chain, path_recs):
    """Combine a chain of path records into a single SubPath."""
    all_segs = []
    for idx in chain:
        sp = path_recs[idx]['subpath']
        all_segs.extend(sp.segments)
    return SubPath(segments=all_segs, closed=False)


# ── Main processing pipeline ─────────────────────────────────────────────

def process_svg(input_path, output_path, args):
    """Process SVG using regex to avoid ElementTree namespace mangling."""
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    stats = {
        'paths_original': 0,
        'paths_removed_short': 0,
        'paths_simplified_to_line': 0,
        'paths_simplified_to_arc': 0,
        'paths_rdp_simplified': 0,
        'paths_kept_unchanged': 0,
        'paths_final': 0,
        'kink_splits': 0,
        'subpaths_merged': 0,
        'chains_formed': 0,
        'paths_chained': 0,
        'segments_original': 0,
        'segments_final': 0,
    }

    # Match <path ... /> elements
    path_re = re.compile(r'<path\b[^>]*/>', re.DOTALL)
    matches = list(path_re.finditer(content))
    stats['paths_original'] = len(matches)
    print(f"Found {len(matches)} path elements")

    # ── Phase 1: Parse all paths and simplify individually ────────────

    # Build records for each <path> match
    records = []  # parallel to matches: {subpaths, simplified, remove}
    for match in matches:
        path_tag = match.group(0)
        d_match = re.search(r'\bd="([^"]*)"', path_tag)
        rec = {'match': match, 'd_match': d_match, 'remove': False,
               'new_d': None, 'kept': None, 'changed': False}

        if not d_match:
            rec['remove'] = True
            stats['paths_removed_short'] += 1
            records.append(rec)
            continue

        d = d_match.group(1)
        subpaths = parse_d(d)
        if not subpaths:
            rec['remove'] = True
            stats['paths_removed_short'] += 1
            records.append(rec)
            continue

        for sp in subpaths:
            stats['segments_original'] += len(sp.segments)

        # Split at kinks (sharp angle changes)
        split_sps = []
        for sp in subpaths:
            split_sps.extend(split_at_kinks(sp, args.kink_angle))
        stats['kink_splits'] += len(split_sps) - len(subpaths)
        kept = split_sps

        # Merge nearby subpath endpoints (within single <path>)
        if not args.no_merge and len(kept) > 1:
            merged = [kept[0]]
            for sp in kept[1:]:
                m = try_merge_subpaths(merged[-1], sp, args.merge_distance)
                if m:
                    merged[-1] = m
                    stats['subpaths_merged'] += 1
                else:
                    merged.append(sp)
            kept = merged

        # Individual simplification
        if not args.no_simplify:
            simplified = []
            for sp in kept:
                result = simplify_to_line(sp, args.line_tolerance)
                if result:
                    simplified.append(result)
                    stats['paths_simplified_to_line'] += 1
                    continue

                result = simplify_to_arc(sp, args.arc_tolerance)
                if result:
                    simplified.append(result)
                    stats['paths_simplified_to_arc'] += 1
                    continue

                if len(sp.segments) > 2:
                    result = simplify_subpath_rdp(sp, args.rdp_tolerance)
                    if len(result.segments) < len(sp.segments):
                        simplified.append(result)
                        stats['paths_rdp_simplified'] += 1
                        continue

                simplified.append(sp)
                stats['paths_kept_unchanged'] += 1
            kept = simplified

        # Remove short subpaths (after simplification)
        if args.min_length > 0:
            kept = [sp for sp in kept if sp.length() >= args.min_length]
            if not kept:
                rec['remove'] = True
                stats['paths_removed_short'] += 1
                records.append(rec)
                continue

        rec['kept'] = kept
        records.append(rec)

    # ── Phase 2: Cross-path endpoint chaining ───────────────────────────

    if not args.no_merge:
        # Build flat list of path records for chaining
        path_recs = []
        for ri, rec in enumerate(records):
            if rec['remove'] or not rec['kept']:
                continue
            for si, sp in enumerate(rec['kept']):
                path_recs.append({
                    'rec_idx': ri,
                    'sp_idx': si,
                    'subpath': sp,
                })

        print(f"Phase 2: chaining {len(path_recs)} subpaths by endpoint proximity...")
        chains = chain_paths_by_endpoints(path_recs, args.merge_distance)

        multi_chains = [c for c in chains if len(c) > 1]
        print(f"  Formed {len(multi_chains)} chains (from {sum(len(c) for c in multi_chains)} paths)")
        stats['chains_formed'] = len(multi_chains)

        for chain in chains:
            if len(chain) <= 1:
                continue

            stats['paths_chained'] += sum(len(c) for c in [chain])

            # Merge chain into single subpath
            merged_sp = merge_chain_to_subpath(chain, path_recs)

            # Re-simplify the merged path
            if not args.no_simplify:
                # Try whole-path simplification first (cheapest output)
                result = simplify_to_line(merged_sp, args.line_tolerance)
                if result:
                    merged_sp = result
                else:
                    result = simplify_to_arc(merged_sp, args.arc_tolerance)
                    if result:
                        merged_sp = result
                    elif len(merged_sp.segments) > 2:
                        # Piecewise: greedily fit arcs/lines along the chain
                        merged_sp = simplify_piecewise(
                            merged_sp, args.arc_tolerance,
                            args.line_tolerance, args.rdp_tolerance)

            # Assign merged subpath to the first record in the chain;
            # remove originals from all affected records
            affected_recs = {}  # rec_idx -> set of sp_idx to remove
            for ci in chain:
                ri = path_recs[ci]['rec_idx']
                si = path_recs[ci]['sp_idx']
                if ri not in affected_recs:
                    affected_recs[ri] = set()
                affected_recs[ri].add(si)

            # Remove the original subpaths by id
            member_sp_ids = set(id(path_recs[ci]['subpath']) for ci in chain)
            first_ri = path_recs[chain[0]]['rec_idx']

            for ri, sp_indices in affected_recs.items():
                rec = records[ri]
                if rec['kept']:
                    rec['kept'] = [sp for sp in rec['kept']
                                   if id(sp) not in member_sp_ids]

            # Add merged subpath to the first record
            if records[first_ri]['kept'] is None:
                records[first_ri]['kept'] = []
            records[first_ri]['kept'].append(merged_sp)

            # Mark empty records for removal
            for ri in affected_recs:
                if not records[ri]['kept']:
                    records[ri]['remove'] = True

    # ── Phase 3: Apply all changes to content string ──────────────────

    # Process in reverse order to preserve offsets
    for rec in reversed(records):
        match = rec['match']
        if rec['remove']:
            content = content[:match.start()] + content[match.end():]
            continue

        kept = rec['kept']
        if not kept:
            content = content[:match.start()] + content[match.end():]
            continue

        d_parts = [subpath_to_d(sp) for sp in kept if sp.segments]
        if not d_parts:
            content = content[:match.start()] + content[match.end():]
            continue

        new_d = " ".join(d_parts)
        for sp in kept:
            stats['segments_final'] += len(sp.segments)

        path_tag = match.group(0)
        d_match = rec['d_match']
        d_rel_start = d_match.start(1)
        d_rel_end = d_match.end(1)
        new_tag = path_tag[:d_rel_start] + new_d + path_tag[d_rel_end:]

        # If path was modified and --mark-color is set, change stroke color
        mark_color = getattr(args, 'mark_color', None)
        if mark_color and new_d != d_match.group(1):
            new_tag = re.sub(
                r'stroke:#[0-9a-fA-F]{3,8}',
                f'stroke:{mark_color}',
                new_tag
            )

        content = content[:match.start()] + new_tag + content[match.end():]
        stats['paths_final'] += 1

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    if args.stats:
        print(f"\n{'─' * 50}")
        print(f"  Original paths:            {stats['paths_original']:>6}")
        print(f"  Removed (short):           {stats['paths_removed_short']:>6}")
        print(f"  Simplified → line:         {stats['paths_simplified_to_line']:>6}")
        print(f"  Simplified → arc:          {stats['paths_simplified_to_arc']:>6}")
        print(f"  RDP simplified:            {stats['paths_rdp_simplified']:>6}")
        print(f"  Kept unchanged:            {stats['paths_kept_unchanged']:>6}")
        print(f"  Kink splits:               {stats['kink_splits']:>6}")
        print(f"  Subpaths merged (intra):   {stats['subpaths_merged']:>6}")
        print(f"  Chains formed (cross):     {stats['chains_formed']:>6}")
        print(f"  Paths chained:             {stats['paths_chained']:>6}")
        print(f"  Final paths:               {stats['paths_final']:>6}")
        print(f"  Original segments:         {stats['segments_original']:>6}")
        print(f"  Final segments:            {stats['segments_final']:>6}")
        print(f"{'─' * 50}")

    return stats


# ── CLI ───────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Normalize and simplify SVG path data.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('input', help='Input SVG file')
    parser.add_argument('output', nargs='?', help='Output SVG file (default: input with -normalized suffix)')
    parser.add_argument('--min-length', type=float, default=5.0,
                        help='Remove paths shorter than this (default: 5.0)')
    parser.add_argument('--arc-tolerance', type=float, default=1.5,
                        help='Max deviation for arc fitting (default: 1.5)')
    parser.add_argument('--line-tolerance', type=float, default=0.8,
                        help='Max deviation for line fitting (default: 0.8)')
    parser.add_argument('--rdp-tolerance', type=float, default=0.5,
                        help='RDP simplification tolerance (default: 0.5)')
    parser.add_argument('--merge-distance', type=float, default=2.0,
                        help='Max gap to merge adjacent subpath endpoints (default: 2.0)')
    parser.add_argument('--kink-angle', type=float, default=60,
                        help='Angle threshold in degrees for splitting paths at kinks (default: 60)')
    parser.add_argument('--no-simplify', action='store_true',
                        help='Skip arc/line/RDP simplification (just remove short paths)')
    parser.add_argument('--no-merge', action='store_true',
                        help='Skip endpoint merging')
    parser.add_argument('--stats', action='store_true', default=True,
                        help='Print statistics (default: on)')
    parser.add_argument('--no-stats', action='store_true',
                        help='Suppress statistics')
    parser.add_argument('--mark-color', type=str, default=None,
                        help='Stroke color for modified paths (e.g. "#0066ff"). '
                             'Unchanged paths keep original color.')

    args = parser.parse_args()
    if args.no_stats:
        args.stats = False

    if not args.output:
        base = args.input.rsplit('.', 1)
        args.output = f"{base[0]}-normalized.svg"

    print(f"Input:  {args.input}")
    print(f"Output: {args.output}")
    print(f"Min path length: {args.min_length}")

    process_svg(args.input, args.output, args)

    # Report file sizes
    import os
    in_size = os.path.getsize(args.input)
    out_size = os.path.getsize(args.output)
    ratio = out_size / in_size * 100
    print(f"\nFile size: {in_size:,} → {out_size:,} bytes ({ratio:.1f}%)")


if __name__ == '__main__':
    main()
