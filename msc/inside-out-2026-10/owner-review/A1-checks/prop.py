import itertools, random
# noisy AND/OR SCM: leaves X~Bern(p_v); edge transmission E_iv~Bern(p_iv); all independent.
def truth(nodes, parents, gamma, pl, pe):
    exo = [('L',v) for v in nodes if not parents[v]] + [('E',i,v) for v in nodes for i in parents[v]]
    prob = {v:0.0 for v in nodes}
    for bits in itertools.product([0,1], repeat=len(exo)):
        w=1.0; a=dict(zip(exo,bits))
        for k,b in a.items():
            p = pl[k[1]] if k[0]=='L' else pe[(k[1],k[2])]
            w *= p if b else 1-p
        X={}
        for v in nodes:
            if not parents[v]: X[v]=a[('L',v)]
            else:
                t=[X[i] and a[('E',i,v)] for i in parents[v]]
                X[v]= int(all(t)) if gamma[v]=='AND' else int(any(t))
            prob[v]+=w*X[v]
    return prob
def propagate(nodes, parents, gamma, pl, pe):
    s={}
    for v in nodes:
        if not parents[v]: s[v]=pl[v]
        elif gamma[v]=='AND':
            r=1.0
            for i in parents[v]: r*=pe[(i,v)]*s[i]
            s[v]=r
        else:
            r=1.0
            for i in parents[v]: r*=1-pe[(i,v)]*s[i]
            s[v]=1-r
    return s
# A1 counterexample: C leaf .5; A=AND(C), B=AND(C), R=AND(A,B), edges 1
nodes=['C','A','B','R']; par={'C':[],'A':['C'],'B':['C'],'R':['A','B']}
g={'A':'AND','B':'AND','R':'AND'}; pl={'C':.5}; pe={(i,v):1.0 for v in nodes for i in par[v]}
print('A1 truth',truth(nodes,par,g,pl,pe)['R'],'prop',propagate(nodes,par,g,pl,pe)['R'])
# example-L1 naive vs correct
nodes=['C','A1','A2','B1','B2','G']; par={'C':[],'A1':[],'A2':[],'B1':['C','A1'],'B2':['C','A2'],'G':['B1','B2']}
g={'B1':'AND','B2':'AND','G':'OR'}; pl={'C':.8,'A1':.9,'A2':.7}; pe={(i,v):1.0 for v in nodes for i in par[v]}
print('naive L1 truth',round(truth(nodes,par,g,pl,pe)['G'],4),'prop',round(propagate(nodes,par,g,pl,pe)['G'],4))
nodes=['C','A1','A2','S','G']; par={'C':[],'A1':[],'A2':[],'S':['A1','A2'],'G':['C','S']}
g={'S':'OR','G':'AND'}; pe={(i,v):1.0 for v in nodes for i in par[v]}
print('correct L1 truth',round(truth(nodes,par,g,pl,pe)['G'],4),'prop',round(propagate(nodes,par,g,pl,pe)['G'],4))
# multitree-not-polytree: a,b leaves; c=AND(a,b), d=OR(a,b) -- skeleton cycle a-c-b-d-a, but no node has 2 parents w/ common ancestor
random.seed(1)
nodes=['a','b','c','d']; par={'a':[],'b':[],'c':['a','b'],'d':['a','b']}; g={'c':'AND','d':'OR'}
mx=0
for _ in range(200):
    pl={'a':random.random(),'b':random.random()}; pe={(i,v):random.random() for v in nodes for i in par[v]}
    T=truth(nodes,par,g,pl,pe); S=propagate(nodes,par,g,pl,pe); mx=max(mx,max(abs(T[v]-S[v]) for v in nodes))
print('multitree non-polytree max err at every node', mx)
# add a root R=AND(c,d): now a has 2 paths to R -> should fail at R
nodes2=nodes+['R']; par['R']=['c','d']; g['R']='AND'
pl={'a':.6,'b':.7}; pe={(i,v):random.random() for v in nodes2 for i in par[v]}
T=truth(nodes2,par,g,pl,pe); S=propagate(nodes2,par,g,pl,pe); print('rooted version R err', T['R']-S['R'])
