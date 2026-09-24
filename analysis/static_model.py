"""Acemoglu-Restrepo, NBER June 2017: reproducible static specialization.

eta -> 0, sigma=0.8, gamma(i)=exp(A*i), log C - chi*L**2/2.
No empirical calibration. Solves labor supply and the endogenous task cutoff.
"""
from pathlib import Path
import csv
import json
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SIGMA, A, B, CHI = 0.8, 5.0, 1.0, 1.0

def brentq(f, lo, hi, xtol=1e-13):
    """Bracketed bisection; name retained for the two existing call sites.

    Pure Python implementation avoids a platform-specific SciPy DLL dependency.
    """
    flo, fhi = f(lo), f(hi)
    if flo == 0: return lo
    if fhi == 0: return hi
    if flo*fhi > 0: raise ValueError('Root must be bracketed')
    for _ in range(200):
        mid=(lo+hi)/2
        fm=f(mid)
        if fm == 0 or hi-lo < xtol: return mid
        if flo*fm < 0: hi=mid
        else: lo, flo=mid, fm
    raise RuntimeError('Bisection did not converge')

def fixed_cutoff(K, J, N=1.0):
    a = J-N+1
    assert 0 < a < 1 and K > 0
    rho = (SIGMA-1)/SIGMA
    G = (math.exp(A*(SIGMA-1)*N)-math.exp(A*(SIGMA-1)*J))/(A*(SIGMA-1))
    x = a**(1/SIGMA)*K**rho
    def share(L):
        z = G**(1/SIGMA)*L**rho
        return z/(x+z)
    L = brentq(lambda L: CHI*L*L-share(L), 1e-9, 1/math.sqrt(CHI), xtol=1e-13)
    S = x+G**(1/SIGMA)*L**rho
    Y = B*S**(1/rho)
    R = B*S**(1/rho-1)*a**(1/SIGMA)*K**(rho-1)
    W = B*S**(1/rho-1)*G**(1/SIGMA)*L**(rho-1)
    return dict(K=float(K), Istar=float(J), N=float(N), L=L, Y=Y, W=W, R=R,
                sL=W*L/Y, G=G, a=a)

def equilibrium(K, I=0.4, N=1.0):
    candidate = fixed_cutoff(K,I,N)
    def gap(q): return math.log(q['W']/q['R'])-A*q['Istar']
    if gap(candidate) >= 0:
        q = candidate
        regime = 'technology-constrained'
    else:
        J = brentq(lambda j: gap(fixed_cutoff(K,j,N)), N-1+1e-7,I,xtol=1e-13)
        q = fixed_cutoff(K,J,N)
        regime = 'cost-minimizing'
    q.update(I=I,regime=regime)
    q['cost_gap'] = gap(q)
    q['new_task_margin'] = q['R']-q['W']/math.exp(A*N)
    q['epsilonL'] = (1-q['sL'])/(1+q['sL'])
    q['LambdaI'] = math.exp(A*(SIGMA-1)*q['Istar'])/q['G']+1/q['a']
    q['productivity'] = B**(SIGMA-1)*((q['W']/math.exp(A*q['Istar']))**(1-SIGMA)-q['R']**(1-SIGMA))/(1-SIGMA)
    q['displacement'] = (1-q['sL'])*q['LambdaI']/(SIGMA+q['epsilonL'])
    q['wage_derivative_formula'] = q['productivity']-q['displacement'] if regime=='technology-constrained' else 0.0
    return q

def main():
    for name in ('results','figures'): (ROOT/name).mkdir(exist_ok=True)
    grid = np.geomspace(0.5,50.0,220)
    rows=[]
    errors=[]
    for K in grid:
        q=equilibrium(K)
        if q['new_task_margin']<=0: continue
        h=1e-5
        hi,lo=equilibrium(K,0.4+h),equilibrium(K,0.4-h)
        q['wage_derivative_numeric']=(math.log(hi['W'])-math.log(lo['W']))/(2*h)
        q['labor_share_derivative']=(hi['sL']-lo['sL'])/(2*h)
        q['employment_derivative']=(hi['L']-lo['L'])/(2*h)
        assert abs(q['R']*K+q['W']*q['L']-q['Y'])<1e-9
        assert abs(CHI*q['L']-q['W']/q['Y'])<1e-9
        assert abs(q['Istar']-min(q['I'],math.log(q['W']/q['R'])/A))<1e-9
        if q['regime']=='technology-constrained':
            errors.append(abs(q['wage_derivative_formula']-q['wage_derivative_numeric']))
            assert q['labor_share_derivative']<0 and q['employment_derivative']<0
        else: assert abs(q['wage_derivative_numeric'])<1e-7
        rows.append(q)
    assert max(errors)<2e-6
    pos=[q for q in rows if q['wage_derivative_formula']>0.3]
    neg=[q for q in rows if q['regime']=='technology-constrained' and q['wage_derivative_formula']< -0.3]
    assert pos and neg
    examples=[pos[len(pos)//2],neg[len(neg)//2],next(q for q in rows if q['regime']=='cost-minimizing')]
    omega,L,chi=sp.symbols('omega L chi',positive=True)
    expression=chi*L/(1-chi*L**2)
    elasticity=sp.simplify(expression/(L*sp.diff(expression,L)))
    assert sp.simplify(elasticity-(1-chi*L**2)/(1+chi*L**2))==0
    with (ROOT/'results/static_sweep.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys()); writer.writeheader(); writer.writerows(rows)
    result={'parameters':dict(sigma=SIGMA,A=A,B=B,chi=CHI,I=0.4,N=1,eta_limit=0),
            'examples':examples,'checks':{'grid_points':len(rows),'max_derivative_error':max(errors),
            'market_clearing':'passed','household_FOC':'passed','cutoff_complementarity':'passed',
            'labor_share_employment_signs':'passed','inactive_automation':'passed','sympy_elasticity':'passed'}}
    (ROOT/'results/verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False,'font.family':'DejaVu Sans'})
    active=[q for q in rows if q['regime']=='technology-constrained']
    fig,ax=plt.subplots(figsize=(10,4.6),layout='constrained')
    for field,label,color in [('productivity','Productivity effect','#127D92'),('displacement','Displacement magnitude','#C66C32'),('wage_derivative_formula','Net wage effect','#172E45')]:
        ax.plot([q['K'] for q in active],[q[field] for q in active],label=label,color=color,lw=2.5)
    ax.axhline(0,color='gray',lw=0.8); ax.set_xscale('log'); ax.set_xlabel('Fixed capital stock K (log scale)'); ax.set_ylabel('Semi-elasticity with respect to I'); ax.legend(frameon=False)
    fig.savefig(ROOT/'figures/wage_decomposition.pdf'); fig.savefig(ROOT/'figures/wage_decomposition.png',dpi=180); plt.close(fig)
    fig,axes=plt.subplots(1,2,figsize=(10,4.3),layout='constrained')
    for ax,field,label in zip(axes,['Istar','sL'],['Adopted task cutoff','Labor income share']):
        ax.plot([q['K'] for q in rows],[q[field] for q in rows],color='#127D92',lw=2.5)
        ax.set_xscale('log'); ax.set_xlabel('Fixed capital stock K (log scale)'); ax.set_ylabel(label)
    axes[0].axhline(0.4,color='#C66C32',ls='--',label='Technical frontier I = 0.4'); axes[0].legend(frameon=False,fontsize=10)
    fig.savefig(ROOT/'figures/adoption_share.pdf'); fig.savefig(ROOT/'figures/adoption_share.png',dpi=180); plt.close(fig)
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
