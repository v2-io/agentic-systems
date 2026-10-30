import random, itertools, sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prop import truth, propagate
def npaths(nodes,par):
    # count[u][v] directed paths u->v
    cnt={u:{v:0 for v in nodes} for u in nodes}
    for u in nodes: cnt[u][u]=1
    for v in nodes:  # topological order = list order
        for u in nodes:
            if u!=v: cnt[u][v]=sum(cnt[u][i] for i in par[v])
    return cnt
random.seed(7)
stats={'multi_exact':0,'multi_total':0,'non_err':0,'non_total':0,'and_ok':0,'or_ok':0,'and_n':0,'or_n':0,'root_tree_iff':0,'root_n':0}
for trial in range(400):
    n=random.randint(3,7)
    nodes=[f'n{i}' for i in range(n)]
    par={nodes[0]:[]}
    for i in range(1,n):
        k=random.choice([0,1,1,2,2,3]); k=min(k,i)
        par[nodes[i]]=random.sample(nodes[:i],k)
    mode=random.choice(['mix','AND','OR'])
    g={v:(random.choice(['AND','OR']) if mode=='mix' else mode) for v in nodes if par[v]}
    if sum(len(par[v]) for v in nodes)+sum(1 for v in nodes if not par[v])>13: continue
    pl={v:random.uniform(.05,.95) for v in nodes if not par[v]}
    pe={(i,v):random.uniform(.05,.95) for v in nodes for i in par[v]}
    T=truth(nodes,par,g,pl,pe); S=propagate(nodes,par,g,pl,pe)
    c=npaths(nodes,par)
    multitree=all(c[u][v]<=1 for u in nodes for v in nodes)
    err=max(abs(T[v]-S[v]) for v in nodes)
    if multitree: stats['multi_total']+=1; stats['multi_exact']+= err<1e-12
    else: stats['non_total']+=1; stats['non_err']+= err>1e-9
    if mode=='AND': stats['and_n']+=1; stats['and_ok']+= all(S[v]<=T[v]+1e-12 for v in nodes)
    if mode=='OR': stats['or_n']+=1; stats['or_ok']+= all(S[v]>=T[v]-1e-12 for v in nodes)
    # rooted check: restrict to ancestors of last node; root exact iff every ancestor has exactly 1 path to root
    r=nodes[-1]; anc=[u for u in nodes if c[u][r]>=1]
    tree=all(c[u][r]==1 for u in anc)
    stats['root_n']+=1; stats['root_tree_iff']+= (tree == (abs(T[r]-S[r])<1e-12))
print(stats)
