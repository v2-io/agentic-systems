#!/usr/bin/env python3
"""Join every not-yet-filed audit working file to the segment(s) it names.

Written 2026-10-30 for the inside-out effort (audits-working-dirs map). For
each markdown file under audits/AUDIT-WORKING-*/ that is not inside a
.integrated/ subdir, find the segment slugs in its filename and say whether
that segment's Working Notes already carry an "Incidental audit gold" block
(the marker the 2026-05-30/31 gold-lift sweep wrote).

Caveat that matters: "S" (swept) means the *segment* carries lifted gold from
*some* audits. An audit dated after 2026-05-31 (628417, 374162, 731548) was not
part of that sweep, so its files are unlifted even when the segment shows S.

Usage:  python3 -I audit-gold-status.py [ASF_ROOT]
"""
import glob
import os
import sys

root = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/src/arch/asf')
os.chdir(root)

segs = {}
for p in glob.glob('0*-core/src/*.md'):
    slug = os.path.basename(p)[:-3]
    with open(p) as fh:
        segs[slug] = ('Incidental audit gold' in fh.read(), p.split('/')[0][:6])

for d in sorted(glob.glob('audits/AUDIT-WORKING-*')):
    for dirpath, _, files in os.walk(d):
        if '.integrated' in dirpath:
            continue
        for f in sorted(files):
            if not f.endswith('.md') or 'quiz' in f or 'prediction' in f:
                continue
            base = f[:-3]
            hits = [s for s in segs if s in base and len(s) > 6]
            hits = [h for h in hits if not any(h != o and h in o for o in hits)]
            if hits:
                tags = ' '.join(f"{h}:{'S' if segs[h][0] else 'u'}/{segs[h][1]}" for h in hits)
                print(d[-6:], os.path.relpath(os.path.join(dirpath, f), d), tags)
