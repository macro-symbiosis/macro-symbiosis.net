"""r10 §5.13 verification script: Branch II (H_0 = 0) non-equilibrium steady-state witness,
plus a Branch I regression against r9 §5.11 (tau-compatibility and elliptic theta-equation).
Exact symbolic checks with sympy (40 checks: 36 witness, 4 regression). Run: python3 r10_branch2_witness_check.py"""
import sympy as sp, itertools as it
x,y,z,tau,kap=sp.symbols('x y z tau kappa_G',positive=True)
X=[x,y,z]; n=3; s=sp.sqrt(2)
A=sp.Function('a')(tau)          # shear amplitude a(tau)
g=sp.diag(z**s*sp.exp(A), z**s*sp.exp(A), sp.exp(-2*A))
gi=g.inv()
R3=range(3)
Gam=[[[sp.simplify(sum(gi[l,m]*(sp.diff(g[m,i],X[j])+sp.diff(g[m,j],X[i])-sp.diff(g[i,j],X[m])) for m in R3)/2) for j in R3] for i in R3] for l in R3]
def cov1(w):   # nabla_mu w_nu -> [mu][nu]
    return [[sp.diff(w[nu],X[mu])-sum(Gam[l][mu][nu]*w[l] for l in R3) for nu in R3] for mu in R3]
def cov2(T):   # nabla_a T_{bc} -> [a][b][c]
    return [[[sp.diff(T[b][c],X[a])-sum(Gam[l][a][b]*T[l][c]+Gam[l][a][c]*T[b][l] for l in R3) for c in R3] for b in R3] for a in R3]
def cov3(U):   # nabla_d U_{abc}
    return [[[[sp.diff(U[a][b][c],X[d])-sum(Gam[l][d][a]*U[l][b][c]+Gam[l][d][b]*U[a][l][c]+Gam[l][d][c]*U[a][b][l] for l in R3) for c in R3] for b in R3] for a in R3] for d in R3]
def Riem():
    Rl=[[[[sp.diff(Gam[r][m][s_],X[n_])-sp.diff(Gam[r][n_][s_],X[m])+sum(Gam[r][n_][l]*Gam[l][m][s_]-Gam[r][m][l]*Gam[l][n_][s_] for l in R3) for n_ in R3] for m in R3] for s_ in R3] for r in R3]
    return Rl  # R^r_{s m n} with convention R^r_{s n m}? use Ric below
Rl=Riem()
Ric=sp.Matrix(3,3,lambda i,j: sp.simplify(sum(Rl[r][i][j][r]-0 for r in R3)))
# sign check: use standard Ric_ij = d_r Gam^r_ij - d_j Gam^r_ir + Gam^r_rl Gam^l_ij - Gam^r_jl Gam^l_ir
Ric=sp.Matrix(3,3,lambda i,j: sp.simplify(sum(sp.diff(Gam[r][i][j],X[r])-sp.diff(Gam[r][i][r],X[j])+sum(Gam[r][r][l]*Gam[l][i][j]-Gam[r][j][l]*Gam[l][i][r] for l in R3) for r in R3)))
Rs=sp.simplify(sum(gi[i,j]*Ric[i,j] for i in R3 for j in R3))
G=sp.simplify(Ric-Rs*g/2)
def ok(e):
    if hasattr(e,'shape'): return all(sp.simplify(c)==0 for c in e)
    return sp.simplify(e)==0
res={}
# 1-2 kinematics
detg=sp.simplify(g.det()); res['theta=0 (det g indep of a)']=ok(sp.diff(detg,tau))
D=sp.simplify(gi*sp.diff(g,tau)/2); res['trace D = 0']=ok(D.trace())
sig_mixed=sp.simplify(D-sp.eye(3)*D.trace()/3); sig_low=sp.simplify(g*sig_mixed)
# stress sector
Phi=sp.Rational(3,4)*z**2
dPhi=[sp.diff(Phi,v) for v in X]; Pi=sp.Matrix(cov1(dPhi))
trPi=sum(gi[i,j]*Pi[i,j] for i in R3 for j in R3); Pih=sp.simplify(Pi-g*trPi/3)
eta=[0,0,-s/(kap*z)]
xi=[sp.simplify(sum(Pih[nu,l]*eta[l] for l in R3)) for nu in R3]
res['xi tau-independent']=all(ok(sp.diff(c,tau)) for c in xi)
res['xi = (1-sqrt2)/(kappa z) dz (closed form)']=ok(xi[0]) and ok(xi[1]) and ok(xi[2]-(1-s)/(kap*z))
Dxi=cov1(xi); divxi=sp.simplify(sum(gi[i,j]*Dxi[i][j] for i in R3 for j in R3))
T=sp.Matrix(3,3,lambda m,v: sp.simplify((Dxi[m][v]+Dxi[v][m])/2-g[m,v]*divxi/2))
res['G = kappa T']=ok(G-kap*T)
res['R = kappa div xi']=ok(Rs-kap*divxi)
res['G not identically 0']=not ok(G)
DDxi=cov2(Dxi)   # nabla_a nabla_b xi_c
lap=[sp.simplify(sum(gi[a,b]*DDxi[a][b][c] for a in R3 for b in R3)) for c in R3]
res['lap xi + Ric xi = 0']=all(ok(lap[c]+sum(Ric[c,l]*sum(gi[l,m]*xi[m] for m in R3) for l in R3)) for c in R3)
# tau-compatibility: kappa dT/dtau = L_Ein[sigma] (theta=0)
S=[[sig_low[i,j] for j in R3] for i in R3]
DS=cov2(S); DDS=cov3(DS)  # DDS[d][a][b][c] = nabla_d nabla_a S_bc
def up(i): return i
# nabla^a nabla_mu S_{nu a} = g^{ad} nabla_d nabla_mu S_{nu a}
L=sp.zeros(3,3)
divdivS=sum(gi[a,d]*gi[b,c]*DDS[d][c][a][b] for a in R3 for b in R3 for c in R3 for d in R3)
SR=sum(gi[a,c]*gi[b,d]*S[c][d]*Ric[a,b] for a in R3 for b in R3 for c in R3 for d in R3)
for m in R3:
    for v in R3:
        t1=sum(gi[a,d]*DDS[d][m][v][a] for a in R3 for d in R3)
        t2=sum(gi[a,d]*DDS[d][v][m][a] for a in R3 for d in R3)
        t3=sum(gi[a,d]*DDS[d][a][m][v] for a in R3 for d in R3)
        L[m,v]=t1+t2-t3-g[m,v]*(divdivS-SR)-Rs*S[m][v]
L=sp.simplify(L)
res['kappa dT/dtau = L_Ein[sigma]']=ok(kap*sp.diff(T,tau)-L)
res['elliptic theta-eq (theta=0): 0 = -kappa d(div xi)/dtau + 2 divdiv sigma - 2 sigma.Ric']=ok(-kap*sp.diff(divxi,tau)+2*divdivS-2*SR)
# hysteresis Hess H0 propto g
Hyst0=z**(1+1/s)/(1+1/s); HH=sp.Matrix(cov1([sp.diff(Hyst0,v) for v in X]))
ratio=[sp.simplify(HH[i,i]/g[i,i]) for i in R3]
res['Hess Hyst0 = lambda g (proportionality; lambda>0 checked separately)']=ok(ratio[0]-ratio[2]) and ok(ratio[1]-ratio[2]) and all(ok(HH[i,j]) for i in R3 for j in R3 if i!=j)
print('lambda =',sp.simplify(ratio[2]))
# F balance with anisotropic K (coordinate components) and zeroth-order sink
k1,k3,r0,C,p0,beta,s0,z1,z2=sp.symbols('k_1 k_3 r_0 C_F p_0 beta_th s_0 z_1 z_2',positive=True)
K=sp.diag(k1,k1,k3)
Fp=(r0*z**(s+1)/(s+1)-C)/(k3*z**s)      # dF/dz
F=sp.integrate(Fp,z)
sqrtg=sp.sqrt(detg)
divKgradF=sp.simplify(sum(sp.diff(sqrtg*sum(K[m,v]*sp.diff(F,X[v]) for v in R3),X[m]) for m in R3)/sqrtg)
res['div(frakK grad F) = R_F = r0 (static, theta=0; frakK = transport tensor)']=ok(divKgradF-r0)
res['F tau-independent']=ok(sp.diff(F,tau))
JW=[-sum(K[m,v]*sp.diff(F,X[v]) for v in R3) for m in R3]
JE=[c/p0 for c in JW]
JEdF=sp.simplify(sum(JE[m]*sp.diff(F,X[m]) for m in R3))
res['J_E.gradF = -k3 F_z^2/p0']=ok(JEdF+k3*Fp**2/p0)
ThetaE=sp.simplify(-beta*JEdF/s0)
print('Theta_E =',ThetaE)
# relational edge (r6 O_6 Eq. [2]-[3]): Phi^(1)=Phi^(2)=3/4 z^2, eta_{1->2} = -eta_{2->1} = (c_J/(1-1/sqrt2)) d_z
a0,gM,gc,tau0=sp.symbols('c_0 gamma_M gamma_c tau_0',positive=True)
cJ=a0*sp.exp(-gc*(tau-tau0))   # decaying coupling amplitude c_J (Branch II: integrable flux)
e12=[0,0,cJ/(1-1/s)]; e21=[0,0,-cJ/(1-1/s)]
J12=[sp.simplify(sum(Pih[nu,l]*e12[l] for l in R3)) for nu in R3]
J21=[sp.simplify(sum(Pih[nu,l]*e21[l] for l in R3)) for nu in R3]
Jb=[sp.simplify((J12[i]-J21[i])/2) for i in R3]          # equal Pi-hats, so J_[1->2] = (J12-J21)/2
res['J_[1->2] = c_J(tau) dz, c_J = c0 exp(-gamma_c (tau-tau0))']=all(ok(Jb[i]-[0,0,cJ][i]) for i in R3)
res['coupling amplitude integrable: int_tau0^oo c_J^2 dtau finite']=sp.integrate(cJ**2,(tau,tau0,sp.oo)).is_finite
Jsum=[J12[i]+J21[i] for i in R3]; res['J_{1->2}+J_{2->1} = 0']=all(ok(c) for c in Jsum)
F12=[[sp.diff(J12[b],X[a])-sp.diff(J12[a],X[b]) for b in R3] for a in R3]
res['F^(1->2) = 0 (curvature bracket inactive)']=all(ok(F12[a][b]) for a in R3 for b in R3)
JbJb=sum(gi[a,b]*Jb[a]*Jb[b] for a in R3 for b in R3)
Mlow=sp.Matrix(3,3,lambda m,v: sp.simplify(gM*(Jb[m]*Jb[v]-g[m,v]*JbJb/3)))
Mmix=sp.simplify(gi*Mlow)
res['Tr M = 0']=ok(Mmix.trace())
ev=[sp.simplify(Mmix[i,i]) for i in R3]
res['M (mixed) = gamma_M c_J^2 g^33 diag(-1/3,-1/3,2/3) (full matrix, finite tau)']=ok(Mmix-gM*cJ**2*gi[2,2]*sp.diag(-sp.Rational(1,3),-sp.Rational(1,3),sp.Rational(2,3)))
res['m+ != -m- (n = 3)']=not ok(ev[2]+ev[0])
# harmonic current on the hollow cylinder: c d(phi), phi = atan2(y,x)
ph=sp.atan2(y,x); sq=sp.sqrt(detg)
divgrad=sp.simplify(sum(sp.diff(sq*sum(gi[i,j]*sp.diff(ph,X[j]) for j in R3),X[i]) for i in R3)/sq)
res['d(phi) co-closed (harmonic 1-form)']=ok(divgrad)
# grad F nonvanishing and Theta_E>0 on [z1,z2] when C > r0 z2^(1+sqrt2)/(1+sqrt2)
res['F_z(z2) < 0 for C_F > r0 z2^(1+sqrt2)/(1+sqrt2) (with the monotonicity check, F_z < 0 on [z1,z2])']=ok(sp.simplify(Fp.subs(C, r0*z2**(s+1)/(s+1) + sp.Symbol('delta',positive=True)).subs(z,z2)*k3*z2**s + sp.Symbol('delta',positive=True)))

# O_2 Eq.[2] with J_geom = 0: d ln Omega/dtau = theta/n = 0  (Omega^{2n} = det g)
Om=sp.simplify(detg**sp.Rational(1,6)); res['O_2 Eq.[2]: d ln Omega/dtau = 0 (J_geom = 0 declared)']=ok(sp.diff(sp.log(Om),tau))
# J_E is not an expansion current in Branch II: div J_E = -r0/p0 != 0 while theta = 0
divJE=sp.simplify(sum(sp.diff(sqrtg*JE[m],X[m]) for m in R3)/sqrtg); res['div J_E = -r0/p0 (nonzero) while theta = 0']=ok(divJE+r0/p0)
# O_7 Eq.[3] u_exp identity with J_geom = u_exp = 0 holds trivially; with J_E it would read -r0/p0 * V != 0
# numerator of dF/dz increasing in z (so the z = z2 check bounds it on [z1, z2])
num=r0*z**(s+1)/(s+1)-C; res['numerator of dF/dz increasing in z']=ok(sp.simplify(sp.diff(num,z)-r0*z**s))
# chi_E -> 1: sigma.sigma -> 0 while <Theta_E> is tau-independent and > 0
sigsq=sp.simplify(sum(sig_mixed[i,j]*sig_mixed[j,i] for i in R3 for j in R3))
print('sigma^mu_nu sigma^nu_mu =',sigsq,' (vanishes as da/dtau -> 0)')
res['Theta_E pointwise tau-independent']=ok(sp.diff(ThetaE,tau))
# O_5 Eq.4 with H0 = 0: g -> G_inf as a -> a_inf, and (1/2) g^-1 dg/dtau -> 0 as da/dtau -> 0
res['(1/2) g^-1 dg/dtau proportional to da/dtau']=ok(sp.simplify(D.subs(sp.Derivative(A,tau),0)))

# ---- additional checks requested by the fresh spine audit ----
res['sigma^mu_nu = (da/dtau)/2 diag(1,1,-2)']=ok(sig_mixed-sp.diff(A,tau)/2*sp.diag(1,1,-2))
res['sigma^mu_nu sigma^nu_mu = (3/2)(da/dtau)^2']=ok(sigsq-sp.Rational(3,2)*sp.diff(A,tau)**2)
res['O_5 Eq.[0] (r7): d sqrt|g| / dtau = 0 (>= 0 in Branch II)']=ok(sp.diff(sp.sqrt(detg),tau))
res['Theta_E = beta k3 F_z^2/(p0 s0)']=ok(ThetaE-beta*k3*Fp**2/(p0*s0))
res['Hessian factor lambda = sqrt2/2 z^(-1+sqrt2/2) e^(2a)']=ok(ratio[2]-s/2*z**(-1+s/2)*sp.exp(2*A))
res['Hessian factor lambda > 0 (a real)']=bool(sp.simplify(ratio[2]).subs(A,sp.Symbol('a_r',real=True)).is_positive)
# cone-preserving drive: along solutions du^2/dtau = (1-u^2)(-dg/dtau vv + 2(1-u^2) a.v)
V=sp.symbols('v1 v2 v3',real=True); Ad=sp.symbols('ad1 ad2 ad3',real=True)
u2=sum(g[i,j]*V[i]*V[j] for i in R3 for j in R3)
av=sum(g[i,j]*Ad[i]*V[j] for i in R3 for j in R3)
f=[(1-u2)*(Ad[m]-av*V[m]) for m in R3]
dg=sp.diff(g,tau); dgvv=sum(dg[i,j]*V[i]*V[j] for i in R3 for j in R3)
dv=[-sum(Gam[m][r][e]*V[r]*V[e] for r in R3 for e in R3)-sum(gi[m,l]*dg[l,k]*V[k] for l in R3 for k in R3)+dgvv*V[m]/2+f[m] for m in R3]
du2=dgvv+sum(sp.diff(g[i,j],X[l])*V[l]*V[i]*V[j] for i in R3 for j in R3 for l in R3)+2*sum(g[i,j]*V[i]*dv[j] for i in R3 for j in R3)
res['drive: du^2/dtau = (1-u^2)(-dg vv + 2(1-u^2) a.v) (u^2=1 invariant)']=ok(sp.expand(du2-(1-u2)*(-dgvv+2*(1-u2)*av)))

# O_3 Eq.[2] damping law for the declared a(tau) = (2 s/g)(1 - exp(-g (tau - tau0)))
gs,ss=sp.symbols('gamma_sigma s_sigma',positive=True)
aexp=(2*ss/gs)*(1-sp.exp(-gs*(tau-tau0)))
sig_e=sig_mixed.subs(sp.Derivative(A,tau),sp.diff(aexp,tau)).subs(A,aexp).doit()
res['O_3 Eq.[2]: d sigma/dtau = -gamma_sigma sigma for the declared a(tau)']=ok(sp.diff(sig_e,tau)+gs*sig_e)
for k,v in res.items(): print(('PASS' if v else 'FAIL'),'-',k)
print('M (mixed) =',Mmix)

# ---------------- Branch I regression: r9 §5.11 metric with H_0 > 0 ----------------
H0=sp.symbols('H_0',positive=True)
gI=sp.exp(2*H0*tau)*sp.diag(z**s*sp.exp(A), z**s*sp.exp(A), sp.exp(-2*A))
def branch1():
    global g,gi,Gam,Ric,Rs
    g=gI; gi=g.inv()
    Gam=[[[sp.simplify(sum(gi[l,m]*(sp.diff(g[m,i],X[j])+sp.diff(g[m,j],X[i])-sp.diff(g[i,j],X[m])) for m in R3)/2) for j in R3] for i in R3] for l in R3]
    Ric=sp.Matrix(3,3,lambda i,j: sp.simplify(sum(sp.diff(Gam[r][i][j],X[r])-sp.diff(Gam[r][i][r],X[j])+sum(Gam[r][r][l]*Gam[l][i][j]-Gam[r][j][l]*Gam[l][i][r] for l in R3) for r in R3)))
    Rs=sp.simplify(sum(gi[i,j]*Ric[i,j] for i in R3 for j in R3))
    th=sp.simplify(sp.diff(sp.log(sp.sqrt(g.det())),tau))
    Dm=sp.simplify(gi*sp.diff(g,tau)/2); sm=sp.simplify(Dm-sp.eye(3)*Dm.trace()/3); sl=sp.simplify(g*sm)
    dP=[sp.diff(Phi,v) for v in X]; P=sp.Matrix(cov1(dP)); tP=sum(gi[i,j]*P[i,j] for i in R3 for j in R3); Ph=sp.simplify(P-g*tP/3)
    xi1=[sp.simplify(sum(Ph[nu,l]*eta[l] for l in R3)) for nu in R3]
    D1=cov1(xi1); dv=sp.simplify(sum(gi[i,j]*D1[i][j] for i in R3 for j in R3))
    T1=sp.Matrix(3,3,lambda m,v: sp.simplify((D1[m][v]+D1[v][m])/2-g[m,v]*dv/2))
    S=[[sl[i,j] for j in R3] for i in R3]; DS=cov2(S); DDS=cov3(DS)
    dd=sum(gi[a,d]*gi[b,c]*DDS[d][c][a][b] for a in R3 for b in R3 for c in R3 for d in R3)
    SR=sum(gi[a,c]*gi[b,d]*S[c][d]*Ric[a,b] for a in R3 for b in R3 for c in R3 for d in R3)
    L=sp.zeros(3,3)
    for m in R3:
        for v in R3:
            L[m,v]=sum(gi[a,d]*(DDS[d][m][v][a]+DDS[d][v][m][a]-DDS[d][a][m][v]) for a in R3 for d in R3)-g[m,v]*(dd-SR)-Rs*S[m][v]
    G1=sp.simplify(Ric-Rs*g/2)
    return {'Branch I regression: theta = 3H_0':ok(th-3*H0),
            'Branch I regression: G = kappa T':ok(G1-kap*T1),
            'Branch I regression: kappa dT/dtau = -(n-2)/n (grad grad theta - g lap theta) + L_Ein[sigma] (theta const)':ok(kap*sp.diff(T1,tau)-sp.simplify(L)),
            'Branch I regression: elliptic theta-equation':ok(sp.Rational(2,3)*Rs*th-(-kap*sp.diff(dv,tau)+2*dd-2*SR))}
for k,v in branch1().items(): print(('PASS' if v else 'FAIL'),'-',k)
