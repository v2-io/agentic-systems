"""Chart-vs-convention discriminator: contexts where Unicode's next code point differs from the conventional next
letter (Greek final sigma, Hebrew final forms, Latin-1 x/÷ inside the letters, ASCII z -> {). Study wording, read-only
harness import; answers to this scratchpad only."""
import json, sys, time, concurrent.futures as cf, pathlib
STUDY = pathlib.Path('/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception')
sys.path.insert(0, str(STUDY / 'harness/seq')); sys.path.insert(0, str(STUDY / 'harness/core'))
import items as IT, parse as P
from judges import make_judge
MINDS = json.load(open(STUDY / 'harness/core/minds.json'))['minds']
OUT = pathlib.Path(sys.argv[0]).parent / 'discrim'
OUT.mkdir(exist_ok=True)
A = [list('οπρ'), list('זחטי'), list('ÓÔÕÖ'), list('òóôõö'), list('wxyz')]
B = [['ρ'], ['י'], ['ל'], ['Ö'], ['z']]
S = []
for n, ctxs in (('A', A), ('B', B)):
    ent = [{'id': i, 'pid': f'{n}{i}', 'shown': c} for i, c in enumerate(ctxs)]
    s = {'sid': f'audit-discrim-{n}', 'kind': 'next', 'factors': {'perp': True, 'tie': False, 'gap': False}, 'entries': ent}
    s['prompt'] = IT.sheet_prompt(s); S.append(s)
def one(args):
    mind, s = args
    return mind, s, make_judge(MINDS[mind])(IT.SYSTEM, s['prompt'])
jobs = [(m, s) for m in ('sonnet55', 'gemini38flash', 'grok46') for s in S]
with cf.ThreadPoolExecutor(3) as ex:
    for mind, s, r in ex.map(one, jobs):
        rec = {'mind': mind, 'sid': s['sid'], 'prompt': s['prompt'], 'result': r, 't': time.time()}
        open(OUT / 'raw.jsonl', 'a').write(json.dumps(rec, ensure_ascii=False) + '\n')
        parsed = P.parse_sheet(r.get('raw') or '', s) if r.get('raw') else {}
        print(mind, s['sid'], {e['pid']: (''.join(e['shown']), v.get('answer')) for e, v in zip(s['entries'], parsed.values())} if parsed else r.get('error'), flush=True)
