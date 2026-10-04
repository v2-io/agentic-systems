"""python3 -m unittest discover -s harness/seq/tests   (from the study root)"""
import json, sys, pathlib, unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import items as I
import parse as P

T = I.make_item("triad", ["①", "⑴", "❶"])

class Rotation(unittest.TestCase):
    def test_each_glyph_in_middle_once(self):
        mids = [I.shown_order(T, r)[1] for r in range(3)]
        self.assertEqual(sorted(mids), sorted(T["glyphs"]))

    def test_rotations_are_orders_of_the_triad(self):
        for r in range(3):
            self.assertEqual(sorted(I.shown_order(T, r)), T["glyphs"])

    def test_fated(self):
        self.assertEqual(I.shown_order(T, 1), I.shown_order(I.make_item("triad", ["❶", "①", "⑴"]), 1))

class Sheets(unittest.TestCase):
    def test_placement_and_prompt(self):
        its = [I.make_item("triad", [chr(0x2460 + 3 * i + j) for j in range(3)]) for i in range(12)]
        pres = [I.presentation(it, r, "t") for it in its for r in range(3)]
        sh = I.build_sheets("t", {i["iid"]: i for i in its}, pres, "triad")
        self.assertEqual(sum(len(s["entries"]) for s in sh), 36)
        for s in sh:
            ids = [e["pid"] for e in s["entries"]]
            iids = [next(p["iid"] for p in pres if p["pid"] == x) for x in ids]
            top = max(iids.count(i) for i in iids)
            if top <= (len(iids) + 1) // 2:   # avoidable: then no two presentations of one item are adjacent
                self.assertFalse(any(iids[j] == iids[j - 1] for j in range(1, len(iids))), "adjacent repeats")
            self.assertLessEqual(len(ids), 5)
            self.assertIn('"s":', s["prompt"])
            self.assertNotIn("magnitude", s["prompt"].lower())
        self.assertTrue(all("factors" in p and "sid" in p for p in pres))

def sheet_of(kind, shown_list):
    return {"kind": kind, "entries": [{"id": n, "pid": f"p{n}", "shown": s} for n, s in enumerate(shown_list)]}

class ParseTriad(unittest.TestCase):
    sh = sheet_of("triad", [["⑴", "❶", "①"]] * 8)
    def run_one(self, ans):
        raw = "noise " + json.dumps({"answers": ans}, ensure_ascii=False)
        return P.parse_sheet(raw, self.sh)

    def test_forms(self):
        r = self.run_one([
            {"id": 0, "seq": ["①", "⑴", "❶"]},
            {"id": 1, "seq": ["#3", "#1", "#2"]},          # positions: ①, ⑴, ❶
            {"id": 2, "two": ["❶", "①"]},
            {"id": 3, "none": True},
            {"id": 4, "seq": ["①", ["⑴", "❶"]]},
            {"id": 5, "seq": [["①", "⑴", "❶"]]},
            {"id": 6, "seq": ["①", "⑴"]},                  # missing a glyph
            {"id": 7, "seq": ["①", "⑴", "⬭"]}])            # echo failure
        a = {k: v.get("answer") for k, v in r.items()}
        self.assertEqual(a["p0"], ("mid", "⑴"))
        self.assertEqual(a["p1"], ("mid", "⑴"))
        self.assertEqual(a["p2"], ("two", "①", "❶"))
        self.assertEqual(a["p3"], ("none",))
        self.assertEqual(a["p4"], ("tie2", "①", "⑴", "❶"))
        self.assertEqual(a["p5"], ("tie3",))
        self.assertEqual(r["p6"]["status"], "unparsed")
        self.assertEqual(r["p7"]["status"], "unparsed")

    def test_conflicting_keys_and_duplicates(self):
        r = self.run_one([{"id": 0, "seq": ["①", "⑴", "❶"], "none": True},
                          {"id": 1, "none": True}, {"id": 1, "none": True}])
        self.assertEqual(r["p0"]["status"], "unparsed")
        self.assertEqual(r["p1"]["why"], "duplicate-id")
        self.assertEqual(r["p2"]["why"], "missing")

    def test_last_answers_object_wins(self):
        raw = '{"answers":[{"id":0,"none":true}]} restart {"answers":[{"id":0,"seq":["①","⑴","❶"]}]}'
        self.assertEqual(P.parse_sheet(raw, self.sh)["p0"]["answer"], ("mid", "⑴"))

class ParseOrder(unittest.TestCase):
    def test_two_lines_extra_gap(self):
        sh = sheet_of("order", [["░", "▫", "▓", "█", "▒", "·"]])
        raw = json.dumps({"answers": [{"id": 0, "seqs": [["░", "▒", "GAP", "█"], ["·", "▫"]], "extra": ["▓"]}]})
        a = P.parse_sheet(raw, sh)["p0"]["answer"]
        self.assertEqual(a["lines"][0], [["░"], ["▒"], "GAP", ["█"]])
        self.assertEqual(a["extra"], ["▓"])
        self.assertEqual(a["omitted"], [])

    def test_glyph_twice_is_unparsed(self):
        sh = sheet_of("order", [["a", "b", "c", "d"]])
        raw = json.dumps({"answers": [{"id": 0, "seqs": [["a", "b", "c"]], "extra": ["a"]}]})
        self.assertEqual(P.parse_sheet(raw, sh)["p0"]["status"], "unparsed")

class ParseNext(unittest.TestCase):
    def test_props(self):
        sh = sheet_of("next", [["☰", "☱", "☳"]])
        raw = json.dumps({"answers": [{"id": 0, "next": ["☷", "⚌"]}]})
        self.assertEqual(P.parse_sheet(raw, sh)["p0"]["answer"], {"proposals": ["☷", "⚌"]})

if __name__ == "__main__":
    unittest.main()
