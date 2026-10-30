import random, sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prop import truth, propagate
random.seed(11)
def anc_or_self(nodes,par):
    A={}
    for v in nodes:
        s={v}
        for i in par[v]: s|=A[i]
        A[v]=s
    return A
res={'AND':[0,0],'OR':[0,0]}; tried=0
while sum(r[1] for r in res.values())<400 and tried<20000:
    tried+=1
    n=random.randint(3,7); nodes=[f'n{i}' for i in range(n)]; par={nodes[0]:[]}
    for i in range(1,n):
        k=min(random.choice([0,1,2,2,3]),i); par[nodes[i]]=random.sample(nodes[:i],k)
    if sum(len(par[v]) for v in nodes)+sum(1 for v in nodes if not par[v])>13: continue
    A=anc_or_self(nodes,par)
    recon=[v for v in nodes if any(A[a]&A[b] for x,a in enumerate(par[v]) for b in par[v][x+1:])]
    if not recon: continue
    t=random.choice(['AND','OR'])
    g={v:(t if v in recon else random.choice(['AND','OR'])) for v in nodes if par[v]}
    if len(set(g.values()))<2: continue  # want genuinely mixed graphs
    pl={v:random.uniform(.05,.95) for v in nodes if not par[v]}
    pe={(i,v):random.uniform(.05,.95) for v in nodes for i in par[v]}
    T=truth(nodes,par,g,pl,pe); S=propagate(nodes,par,g,pl,pe)
    ok=all(S[v]<=T[v]+1e-12 for v in nodes) if t=='AND' else all(S[v]>=T[v]-1e-12 for v in nodes)
    res[t][0]+=ok; res[t][1]+=1
print(res)
