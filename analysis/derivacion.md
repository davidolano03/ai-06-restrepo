# Automatización: salario, empleo y participación laboral

Fuente: Acemoglu y Restrepo, NBER 22252, revisión de junio de 2017, pp. 6–14 (PDF 8–16). La versión publicada en AER en 2018 tiene título y paginación diferentes.

## Modelo y condiciones

Las tareas pertenecen a $[N-1,N]$, de medida uno. Crear una tarea en $N$ sustituye la tarea inferior: no aumenta la medida total. La productividad laboral $\gamma(i)>0$ es estrictamente creciente. El capital puede producir tareas $i\le I$, pero solo se utiliza si resulta rentable. El umbral efectivo es $I^*=\min\{I,\widetilde I\}$, donde $W/R=\gamma(\widetilde I)$.

La empresa competitiva minimiza el coste por tarea, comparando $R$ con $W/\gamma(i)$. El hogar elige consumo y empleo con preferencias $[(Ce^{-\nu(L)})^{1-\theta}-1]/(1-\theta)$, presupuesto $C=RK+WL$ y condición $\nu'(L)=W/C$. Se imponen regularidad, convexidad y la condición de concavidad de la ecuación (4). El capital es fijo en la comparación estática. La hipótesis 2 exige $\eta\to0$ o $\zeta=1$; $\widehat\sigma=\sigma(1-\eta)+\zeta\eta>0$. La hipótesis 3 restringe capital para que $R>W/\gamma(N)$ y las nuevas tareas se adopten.

## Derivación que conviene verificar a mano

Trabajar en el régimen estricto $N-1<I^*=I<\widetilde I$, con $N$ y $K$ constantes. Definir

$$G=\int_I^N\gamma(i)^{\widehat\sigma-1}\,di,\quad a=I-N+1>0,\quad\Lambda_I=\gamma(I)^{\widehat\sigma-1}/G+1/a>0.$$

De la demanda relativa, ecuación (13),

$$\ln\omega+\frac1{\widehat\sigma}\ln L^s(\omega)=\left(\frac1{\widehat\sigma}-1\right)\ln K+\frac1{\widehat\sigma}\ln(G/a),\qquad\omega=W/(RK).$$

Aplicar Leibniz: $dG/dI=-\gamma(I)^{\widehat\sigma-1}$. Si $\varepsilon_L=d\ln L^s/d\ln\omega>0$,

$$\frac{d\ln\omega}{dI}=-\frac{\Lambda_I}{\widehat\sigma+\varepsilon_L}<0.$$

Como $s_L=\omega L/(1+\omega L)$,

$$\frac{ds_L}{dI}=s_L(1-s_L)(1+\varepsilon_L)\frac{d\ln\omega}{dI}<0,\qquad\frac{d\ln L}{dI}=\varepsilon_L\frac{d\ln\omega}{dI}<0.$$

Pero estas desigualdades no establecen el signo del salario real. La Proposición 3 separa productividad y desplazamiento:

$$g_I\equiv\left.\frac{\partial\ln Y}{\partial I}\right|_{K,L}=\frac{B^{\widehat\sigma-1}}{1-\widehat\sigma}\left[\left(\frac W{\gamma(I)}\right)^{1-\widehat\sigma}-R^{1-\widehat\sigma}\right]>0,$$

$$\frac{d\ln W}{dI}=g_I-\underbrace{(1-s_L)\frac{\Lambda_I}{\widehat\sigma+\varepsilon_L}}_{D_I>0}.$$

Para $\widehat\sigma=1$ debe tomarse el límite continuo $g_I=\ln[W/(R\gamma(I))]$, no dividir entre cero.

**Condición exacta:** el salario aumenta si y solo si $g_I>D_I$; queda constante si son iguales; cae si $g_I<D_I$. La productividad es parcial, manteniendo ambos factores constantes; el salario responde en equilibrio con empleo endógeno. No confundir $g_I$ con la variación total de producción.

Si $I^*=\widetilde I<I$, una pequeña ampliación de $I$ no cambia la asignación y las derivadas respecto de $I$ son cero. En $I=\widetilde I$ hay que distinguir derivadas laterales. Crear tareas eleva productividad y demanda relativa laboral bajo las condiciones anteriores.

## Comprobación computacional

`static_model.py` especializa $\eta\to0$, $\sigma=0.8$, $\gamma(i)=e^{5i}$, $B=1$, $\nu(L)=L^2/2$ y $\theta=1$. Entonces $C=Y$, $L=W/Y$ y $L^2=s_L$. La oferta implícita cumple $\omega=L/(1-L^2)$, de donde $\varepsilon_L=(1-L^2)/(1+L^2)>0$.

El programa resuelve la oferta laboral y el umbral endógeno. Verifica vaciado de mercados, condición del hogar, complementariedad del umbral y derivadas por diferencias centrales. Los parámetros son ilustrativos; no son estimaciones empíricas ni una calibración del paper. Los resultados solo se consideran verificados cuando existe la salida de ejecución correspondiente.

## Largo plazo y tecnología endógena

La Proposición 6 exige $\gamma(i)=e^{Ai}$ con $A>0$, hipótesis 2, $\widehat\sigma>\zeta$ y una oferta de científicos suficientemente pequeña $S<\bar S$. Si $\rho>\bar\rho$ y $\kappa_I/\kappa_N>\bar\kappa$, existe un BGP interior único con $n=N-I\in(\bar n(\rho),1)$ y $\kappa_Iv_I(n)=\kappa_Nv_N(n)$. Para $\theta=0$ se afirma estabilidad global de trayectoria de silla; para $\theta>0$, unicidad local y estabilidad asintótica de trayectoria de silla. No es convergencia global desde cualquier condición cuando $\theta>0$.

Si $\rho<\bar\rho$ existe un BGP de automatización completa. Para $\rho>\bar\rho$, las razones de productividad innovadora entre los dos umbrales pueden producir múltiples BGP; por debajo del umbral inferior se obtiene el BGP sin automatización. Las igualdades en los umbrales no quedan resueltas por estos enunciados estrictos. Los símbolos de umbral dependen del modelo: no son valores numéricos universales.

La estabilización tras un shock transitorio de automatización no implica neutralidad de un cambio permanente de $\kappa_I/\kappa_N$: el Corolario 2 predice menor empleo y participación laboral en el nuevo BGP interior.
