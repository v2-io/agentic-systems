# KR C.1 / C.2, item C1 -- Part I round-3 independent check: the scripts behind reviews/part-i-round-3-check-1.md.
# Four independent programs, concatenated; run each section separately with python3 -I (needs numpy, scipy, mpmath).
# Methods chosen to differ from the integrator: series by log-space summation, t-form integral,
# grid search, bisection, finite-difference radial BVP, Crank-Nicolson survival PDE.

# ======================= section v1 =======================
# Independent: series by direct mpmath summation (log-space), integral by the t-form
# alphaPhi0 = int_0^1 t^{n-1} (e^{k(1-t^2)}-1)/(1-t^2) dt  (different from integrator's G/m form)
from mpmath import mp, mpf, quad, exp, log, euler, sqrt, pi, gamma, loggamma, rf, expm1, inf, nsum
mp.dps = 40
def ser(k, n):
    k = mpf(k); h = mpf(n)/2
    s = mpf(0); term_log = mpf(0); j = 1
    # term_k = k^j/(j (h)_j)
    while True:
        lt = j*log(k) - log(j) - (loggamma(h+j) - loggamma(h))
        t = exp(lt); s += t
        if j > 10 and t < mpf(10)**(-45)*s: break
        j += 1
    return s/2
def tint(k, n):
    k = mpf(k)
    f = lambda t: t**(n-1)*(expm1(k*(1-t*t))/(1-t*t) if t < 1 else k)
    return quad(f, [0, mpf(1)/2, mpf(9)/10, 1])
# Doob/Brownian check: kappa->0 gives kappa/n
print("small kappa", ser('1e-8', 3)/mpf('1e-8'), 1/mpf(3))
for n, k in [(1, .5), (2, 4), (3, 1.5), (3, 6), (10, 5), (20, 40), (100, 50), (5, 9)]:
    print("series vs t-integral", n, k, mp.nstr(ser(k, n), 15), mp.nstr(tint(k, n), 15))
print("threshold values:")
for n in [1, 2, 3, 5, 10, 20, 50, 100, 1000]:
    print(n, mp.nstr(ser(mpf(n)/2, n), 6))
print("two-term asymptotic:")
for n in [1, 10, 100, 1000, 10**4, 10**5, 10**6]:
    v = ser(mpf(n)/2, n); a0 = (log(n)+euler)/4; a1 = sqrt(pi)/(3*sqrt(n))
    print(n, mp.nstr(v, 10), mp.nstr(a0+a1, 10), "r1*sqrt n", mp.nstr((v-a0)*sqrt(n), 6), "r2*n", mp.nstr((v-a0-a1)*n, 6))
print("n=3 margin:", [mp.nstr(ser(1.5+d, 3), 4) for d in [0, 1, 2, 4, 6]])
asym = lambda k, n: gamma(mpf(n)/2)/2*mpf(k)**(-mpf(n)/2)*exp(k)
print("exact/asym (2,4),(2,16):", mp.nstr(ser(4, 2)/asym(4, 2), 4), mp.nstr(ser(16, 2)/asym(16, 2), 4))
for n in [1, 2, 3, 4, 5, 6, 10, 20, 50, 100, 1000]:
    print("asym/exact n=", n, [mp.nstr(asym(k, n)/ser(k, n), 4) for k in [mpf(n)/4, mpf(n)/2, mpf(n)]])
print("(100,40):", mp.nstr(asym(40, 100)/ser(40, 100), 4), "(20,5)", mp.nstr(asym(5, 20)/ser(5, 20), 4), "(100,25)", mp.nstr(asym(25, 100)/ser(25, 100), 5))
# check over every n 1..1000 at n/4 over-estimates
bad = [n for n in range(1, 1001) if asym(mpf(n)/4, n) <= ser(mpf(n)/4, n)]
print("n with asym<=exact at n/4:", bad[:10])
flip = [n for n in range(1, 60) if (asym(mpf(n)/2, n) > ser(mpf(n)/2, n))]
print("n<60 with asym>exact at n/2:", flip)

# ======================= section v2 =======================
import numpy as np
from mpmath import mp, mpf, log, loggamma, exp, findroot
mp.dps = 30
def g(k, n):  # alpha*Phi0, series by summation
    k = mpf(k); h = mpf(n)/2; s = mpf(0); j = 1
    while True:
        t = exp(j*log(k) - log(j) - (loggamma(h+j)-loggamma(h))); s += t
        if j > 10 and t < mpf(10)**-35*s: break
        j += 1
    return s/2
# Gain: fixed channel. Phi0(a) = g(kappa(a), n)/a. Grid search (independent of bounded minimizer)
se, sn = 1.0, 0.5; K = se/sn
for n in [1, 3]:
    for R in [1.0, 1.5, 2.0, 3.0]:
        kap = lambda a: a*R*R/(se**2 + a*a*sn**2)
        al = np.linspace(0.02, 1.6, 3161)*K
        P = np.array([float(g(kap(a), n))/a for a in al])
        i = P.argmax()
        print("n", n, "kapK", round(kap(K), 3), "argmax/K", round(al[i]/K, 3), "max", round(P[i], 4), "at K", round(float(g(kap(K), n))/K, 4),
              "monotone past K:", bool(np.all(np.diff(P[al >= K]) < 0)))
R = 1.0; kap = lambda a: a*R*R/(se**2 + a*a*sn**2)
print("Phi0 at 0.5,0.8,1,1.25,2 K:", [round(float(g(kap(f*K), 1))/(f*K), 3) for f in [0.5, 0.8, 1, 1.25, 2]])
# large kappa(K): maximizer -> K ?
for R in [5.0, 8.0]:
    kap = lambda a: a*R*R/(se**2 + a*a*sn**2)
    al = np.linspace(0.8, 1.05, 2501)*K
    P = np.array([float(g(kap(a), 1)/a) for a in al]); print("kapK", kap(K), "argmax/K", al[P.argmax()]/K)
# doubling increments
for n, ks in [(3, [2.5, 6, 12]), (100, [52, 60, 80, 120])]:
    for k in ks:
        tgt = 2*g(k, n)
        # bisection
        lo, hi = mpf(k), mpf(k)+40
        for _ in range(100):
            mid = (lo+hi)/2
            if g(mid, n) < tgt: lo = mid
            else: hi = mid
        print("double", n, k, mp.nstr(lo-k, 4), "leading formula", round(float(np.log(2)/(1-n/(2*k))), 2))

# ======================= section v3 =======================
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve, splu
# Dip: radial BVP 0.5 s^2 (phi'' + (n-1)/r phi') - g(r) r phi' = -1, phi'(0)=0, phi(R)=0
# Finite differences on r in (0,R] (independent of AVP quadrature)
def radial_mean_exit(gfun, n, s, R, N):
    r = np.linspace(0, R, N+1); h = r[1]-r[0]
    A = np.zeros((N, N)); b = -np.ones(N)
    # node 0: by symmetry phi''(0)*(n) * 0.5 s^2 = -1 (L'Hopital: (n-1)/r phi' -> (n-1) phi'')
    A[0, 0] = -2*n*0.5*s*s/h**2; A[0, 1] = 2*n*0.5*s*s/h**2
    for i in range(1, N):
        ri = r[i]; drift = -gfun(ri)*ri + 0.5*s*s*(n-1)/ri
        A[i, i-1] = 0.5*s*s/h**2 - drift/(2*h)
        A[i, i] = -s*s/h**2
        if i+1 < N: A[i, i+1] = 0.5*s*s/h**2 + drift/(2*h)
    from scipy.sparse import csr_matrix
    phi = spsolve(csr_matrix(A), b)
    return phi[0]
dip = lambda r: 2.0 if 0.485 <= r <= 0.515 else 5.0
for N in [4000, 16000, 64000]:
    print(N, radial_mean_exit(np.vectorize(dip), 2, 1.0, 1.0, N), radial_mean_exit(lambda r: 2.0, 2, 1.0, 1.0, N), radial_mean_exit(lambda r: 5.0, 2, 1.0, 1.0, N))

# ======================= section v4 =======================
# Survival u(t,x)=P_x(tau>t) for 1D OU on [-R,R]: u_t = s^2/2 u_xx - a x u_x, u(+-R)=0, u(0,x)=1
# Crank–Nicolson time-stepping (independent of spectral solve); also mean exit by quadrature
import numpy as np
from scipy.sparse import diags, identity
from scipy.sparse.linalg import splu
from mpmath import mp, mpf, quad, exp
def surv(a, s, R, Ts, N=2001, dt=0.05):
    x = np.linspace(-R, R, N+2)[1:-1]; h = x[1]-x[0]
    lo = s*s/2/h**2 + a*x[1:]/(2*h); up = s*s/2/h**2 - a*x[:-1]/(2*h)
    L = diags([lo, -s*s/h**2*np.ones(N), up], [-1, 0, 1], format='csc')
    I = identity(N, format='csc')
    A = splu((I - dt/2*L).tocsc()); B = (I + dt/2*L).tocsr()
    u = np.ones(N); t = 0.0; out = []; j0 = N//2
    # first few steps implicit Euler to damp CN boundary-layer oscillation
    Ae = splu((I - dt/4*L).tocsc())
    for _ in range(4): u = Ae.solve(u); t += dt/4
    for T in Ts:
        while t < T - 1e-9:
            u = A.solve(B @ u); t += dt
        out.append(1-u[j0])
    return out
def Phi0(a, s, R):
    a, s, R = mpf(a), mpf(s), mpf(R)
    m = lambda u: exp(-a*u*u/s/s)
    return float(2/s/s*quad(lambda u: quad(m, [0, u])/m(u), [0, R]))
for a, s, R in [(1.0, 0.3, 1.0), (0.5, 0.2, 0.8), (1.0, 0.5, 1.0)]:
    p = Phi0(a, s, R)
    print(a, s, R, "kappa", round(a*R*R/s/s, 2), "Phi0", round(p, 1), [round(v, 3) for v in surv(a, s, R, [50, 200, 800, 3200])])

