import json,glob,collections,bisect,sys
sys.path.insert(0,'.')
SEAL=set("▁▂▃▄▅▆▇█🮆🮅🮄▀🮃🮂▔▉")
VOID=set(json.load(open('data/rounds/VOID.json'))['rounds'])
blocks=[]
for l in open('data/unicode/Blocks-16.0.0.txt'):
    l=l.split('#')[0].strip()
    if not l: continue
    r,n=l.split(';'); a,b=r.split('..'); blocks.append((int(a,16),int(b,16),n.strip()))
starts=[b[0] for b in blocks]
def blk(ch):
    o=ord(ch); i=bisect.bisect_right(starts,o)-1
    return blocks[i][2] if i>=0 and blocks[i][0]<=o<=blocks[i][1] else None
seen=set(); recs=[]
for f in sorted(glob.glob('data/answers/*.jsonl')):
    for l in open(f):
        r=json.loads(l)
        if r.get('aid') in seen: continue
        seen.add(r['aid'])
        if r.get('round') in VOID and r.get('outcome') in (None,'call-failed'): continue
        recs.append(r)
print('kinds by era', collections.Counter((r.get('era'),r['kind']) for r in recs).most_common())
# (a) inhibit: chart's next glyph after the context's last, in the context's direction
acc=collections.defaultdict(lambda: collections.Counter())
for r in recs:
    if r['kind']!='inhibit' or (r.get('tags') or {}).get('control'): continue
    c=r['context']; x=r.get('candidate')
    if not x or len(c)<2 or r['outcome'] not in ('yes','no'): continue
    if SEAL & (set(c)|{x}): continue
    d=ord(c[-1])-ord(c[-2])
    if d==0: continue
    s=1 if d>0 else -1
    if ord(x)!=ord(c[-1])+s: continue
    same = blk(x)==blk(c[-1])
    run_blocks=set(blk(g) for g in c)
    key=('same-block' if same else 'cross-block')
    acc[(r['family'],key)][r['outcome']]+=1
print('\n(a) inhibit acceptance of the chart next glyph')
for k in sorted(acc): v=acc[k]; n=v['yes']+v['no']; print(k, n, round(v['yes']/n,3) if n else None)
print('\nexample triad-era triad:', json.dumps([r for r in recs if r['era']=='triad' and r['kind']=='triad'][0],ensure_ascii=False)[:400])
def mid(r):
    a=r.get('answer')
    if isinstance(a,list) and len(a)==2 and a[0]=='mid': return a[1]
    if isinstance(a,dict) and 'mid' in a: return a['mid']
    return None
tri=collections.defaultdict(collections.Counter)
cls_of=lambda g:len(set(blk(x) for x in g))
for r in recs:
    if r['kind']!='triad': continue
    g=r.get('shown') or r['context']
    if len(g)!=3 or SEAL & set(g): continue
    m=mid(r)
    if m is None or m not in g: continue
    med=sorted(g,key=ord)[1]
    nb=cls_of(g)
    # within 2-block: is the median the lone glyph in its block? (impossible since blocks are contiguous) check
    tri[(nb,)]['dep' if m!=med else 'med']+=1
    tri[(nb,r['family'])]['dep' if m!=med else 'med']+=1
print('\n(b) triad middles departing from the code-point median, by distinct Unicode blocks in the triple')
for k in sorted(tri,key=str): v=tri[k]; n=sum(v.values()); print(k, n, round(v['dep']/n,3))
two=collections.defaultdict(collections.Counter)
for r in recs:
    if r['kind']!='triad': continue
    g=r.get('shown') or r['context']
    if len(g)!=3 or SEAL & set(g) or cls_of(g)!=2: continue
    m=mid(r)
    if m is None or m not in g: continue
    bs=collections.Counter(blk(x) for x in g)
    lone=[x for x in g if bs[blk(x)]==1][0]
    med=sorted(g,key=ord)[1]
    t='median' if m==med else ('lone-in-middle (splits the same-block pair)' if m==lone else 'other same-block glyph in middle')
    two['all'][t]+=1; two[r['family']][t]+=1
print('\n(c) two-block triples: which middle')
for k,v in two.items(): n=sum(v.values()); print(k,n,{t:round(c/n,3) for t,c in v.items()})
