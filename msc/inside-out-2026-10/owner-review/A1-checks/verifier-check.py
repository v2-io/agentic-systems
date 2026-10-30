import itertools, random
random.seed(1)

def rand_dag(n, pedge):
    pa = {v: [u for u in range(v) if random.random() < pedge] for v in range(n)}
    typ = {v: random.choice(['AND','OR']) for v in range(n)}
    return pa, typ

def exog(pa):
    leaves = [v for v in pa if not pa[v]]
    edges = [(u,v) for v in pa for u in pa[v]]
    return leaves, edges

def exact(pa, typ, pl, pe, clamp=None):
    leaves, edges = exog(pa)
    vars_ = [('L',l) for l in leaves] + [('E',e) for e in edges]
    prob = {('L',l): pl[l] for l in leaves}; prob.update({('E',e): pe[e] for e in edges})
    n = len(pa); P = [0.0]*n
    for bits in itertools.product([0,1], repeat=len(vars_)):
        w = 1.0
        for b, x in zip(bits, vars_):
            w *= prob[x] if b else 1-prob[x]
        val = dict(zip(vars_, bits)); X = {}
        for v in range(n):
            if not pa[v]: X[v] = val[('L',v)]
            else:
                ins = [X[u] and val[('E',(u,v))] for u in pa[v]]
                X[v] = int(all(ins)) if typ[v]=='AND' else int(any(ins))
        for v in range(n): P[v] += w*X[v]
    return P

def fwd(pa, typ, pl, pe):
    s = {}
    for v in range(len(pa)):
        if not pa[v]: s[v] = pl[v]
        elif typ[v]=='AND':
            x=1.0
            for u in pa[v]: x *= pe[(u,v)]*s[u]
            s[v]=x
        else:
            x=1.0
            for u in pa[v]: x *= 1-pe[(u,v)]*s[u]
            s[v]=1-x
    return s

def npaths(pa, a, b):
    # number of directed paths a->b
    memo={}
    def f(x):
        if x==a: return 1
        if x in memo: return memo[x]
        memo[x]=sum(f(u) for u in pa[x]); return memo[x]
    return f(b)

def unique_paths(pa, v):
    return all(npaths(pa,u,v)<=1 for u in range(v+1))

def anc_or_self(pa, v):
    S={v}; st=[v]
    while st:
        x=st.pop()
        for u in pa[x]:
            if u not in S: S.add(u); st.append(u)
    return S

def reconv(pa, v):
    ps=pa[v]
    for i in range(len(ps)):
        for j in range(i+1,len(ps)):
            if anc_or_self(pa,ps[i]) & anc_or_self(pa,ps[j]): return True
    return False

bad_iff=0; bad_sign_all=0; bad_sign_reconv=0; checked=0; sign_cases={'AND':0,'OR':0}
for trial in range(3000):
    n = random.randint(2,6)
    pa, typ = rand_dag(n, 0.5)
    leaves, edges = exog(pa)
    if len(leaves)+len(edges) > 14: continue
    pl = {l: random.uniform(0.05,0.95) for l in leaves}
    pe = {e: random.uniform(0.05,0.95) for e in edges}
    P = exact(pa,typ,pl,pe); s = fwd(pa,typ,pl,pe); checked+=1
    for v in range(n):
        ex = abs(P[v]-s[v])<1e-12
        if ex != unique_paths(pa,v): bad_iff+=1
    internal=[v for v in range(n) if len(pa[v])>=2]
    # all-AND / all-OR (multi-parent internal nodes)
    if internal and all(typ[v]=='AND' for v in internal):
        if any(s[v]>P[v]+1e-12 for v in range(n)): bad_sign_all+=1
    if internal and all(typ[v]=='OR' for v in internal):
        if any(s[v]<P[v]-1e-12 for v in range(n)): bad_sign_all+=1
    # strengthening: only reconvergence nodes' types matter
    R=[v for v in range(n) if reconv(pa,v)]
    if R and len(set(typ[v] for v in R))==1 and len(set(typ[v] for v in internal))>1:
        t=typ[R[0]]; sign_cases[t]+=1
        if t=='AND' and any(s[v]>P[v]+1e-12 for v in range(n)): bad_sign_reconv+=1
        if t=='OR' and any(s[v]<P[v]-1e-12 for v in range(n)): bad_sign_reconv+=1
print("graphs checked", checked, "iff violations", bad_iff, "all-type sign violations", bad_sign_all)
print("mixed graphs with single reconvergence type:", sign_cases, "violations", bad_sign_reconv)

# triangle a->b, a->c, b->c: strict-ancestor reading of multitree condition
pa={0:[],1:[0],2:[0,1]}; typ={0:'AND',1:'AND',2:'OR'}
pl={0:0.5}; pe={(0,1):0.7,(0,2):0.6,(1,2):0.8}
print("triangle exact vs fwd at c:", exact(pa,typ,pl,pe)[2], fwd(pa,typ,pl,pe)[2])

# mixed graph sign flip: root OR(X,Y), X=AND(C,C) via passthroughs, Y=OR(D,D)
# nodes: 0=C,1=A1(C),2=A2(C),3=X=AND(1,2),4=D,5=B1(D),6=B2(D),7=Y=OR(5,6),8=root=OR(3,7)
pa={0:[],1:[0],2:[0],3:[1,2],4:[],5:[4],6:[4],7:[5,6],8:[3,7]}
typ={0:'AND',1:'AND',2:'AND',3:'AND',4:'AND',5:'AND',6:'AND',7:'OR',8:'OR'}
pe={(u,v):1.0 for v in pa for u in pa[v]}
for c,d in [(0.5,0.01),(0.01,0.5)]:
    pl={0:c,4:d}; print("mixed c,d=",c,d," fwd-exact at root:", fwd(pa,typ,pl,pe)[8]-exact(pa,typ,pl,pe)[8])

# L1 distributivity with soft C-edge credences (q<1) absorbed into branch
c,d1,d2,q1,q2,r1,r2,g1,g2=0.8,0.9,0.7,0.6,0.5,0.95,0.85,0.9,0.8
pa={0:[],1:[],2:[],3:[0,1],4:[0,2],5:[3,4]}; typ={0:'AND',1:'AND',2:'AND',3:'AND',4:'AND',5:'OR'}
pl={0:c,1:d1,2:d2}; pe={(0,3):q1,(1,3):r1,(0,4):q2,(2,4):r2,(3,5):g1,(4,5):g2}
truth=exact(pa,typ,pl,pe)[5]
rewritten = c*(1-(1-g1*q1*r1*d1)*(1-g2*q2*r2*d2))
print("L1 with C-edge credences <1: truth", truth, "tree rewrite", rewritten)

# cutset conditioning on an internal node whose ancestor also reaches root another way
# 0=L leaf, 1=C=AND(L) , 2=A=AND(C), 3=B=AND(C), 4=Z=AND(L), 5=root=AND(A,B,Z)
pa={0:[],1:[0],2:[1],3:[1],4:[0],5:[2,3,4]}; typ={v:'AND' for v in pa}
pl={0:0.6}; pe={(u,v):0.8 for v in pa for u in pa[v]}
truth=exact(pa,typ,pl,pe)[5]
sC=fwd(pa,typ,pl,pe)[1]
def fwd_clamped(cval):
    s={0:pl[0],1:cval}
    s[2]=pe[(1,2)]*s[1]; s[3]=pe[(1,3)]*s[1]; s[4]=pe[(0,4)]*s[0]
    return s[2]*pe[(2,5)]*s[3]*pe[(3,5)]*s[4]*pe[(4,5)]
print("cutset on internal C with shared ancestor: truth", truth, "naive 2-pass", sC*fwd_clamped(1)+(1-sC)*fwd_clamped(0))

# 'enters as p^N' check: OR of two copies of C
p=0.3; print("OR(C,C) fwd", 1-(1-p)**2, "p^2", p**2, "truth", p)
