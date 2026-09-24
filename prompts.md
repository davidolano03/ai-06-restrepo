# Prompts reconstruidos y registro técnico

Los siguientes diálogos son **reconstrucciones didácticas**, redactadas para explicar las preguntas económicas y las decisiones del trabajo. No son una transcripción literal de mensajes del estudiante, ni se presentan como tal. Se omiten instrucciones personales. Esta elección no satisface literalmente el requisito de prompts «raw» de la consigna; el registro técnico auténtico de la corrida se conserva por separado en `lean/audit/run_commands.md` y sus logs.

## 1. Lectura del modelo — reconstrucción

**Prompt:** Explica qué determina la asignación de tareas a capital y trabajo en la revisión NBER de junio de 2017. Distingue posibilidad tecnológica y adopción.

**Respuesta:** El capital puede realizar tareas hasta $I$, pero las empresas solo lo usan cuando su coste $R$ no supera el coste laboral efectivo $W/\gamma(i)$. El umbral adoptado es $I^*=\min\{I,\widetilde I\}$, donde $\gamma(\widetilde I)=W/R$. Aumentar una frontera que no limita la adopción no cambia marginalmente el equilibrio.

## 2. La pregunta trampa — reconstrucción

**Prompt:** ¿La automatización necesariamente reduce salarios y participación laboral? Expón las condiciones y una desigualdad que determine el signo del salario.

**Respuesta:** No hay una respuesta única para ambos objetos. Bajo los supuestos estáticos y con frontera tecnológica vinculante, empleo y participación laboral caen. El salario responde según $d\ln W/dI=g_I-D_I$. Aumenta si la productividad supera el desplazamiento. Si la frontera no es vinculante, el efecto marginal es cero. Tampoco deben confundirse estas comparaciones con el ajuste de capital a largo plazo.

## 3. Comprobación analítica — reconstrucción

**Prompt:** Diferencia la ecuación de demanda relativa, mantén constantes capital y frontera de nuevas tareas y explica cómo verificar el signo de la participación laboral a mano.

**Respuesta:** La regla de Leibniz da $dG/dI=-\gamma(I)^{\widehat\sigma-1}$. Por tanto $(\widehat\sigma+\varepsilon_L)d\ln\omega/dI=-\Lambda_I$. Como $s_L=\omega L/(1+\omega L)$, su derivada tiene el mismo signo que la respuesta relativa. Esta derivación no determina por sí sola el signo del salario real.

## 4. Experimento reproducible — reconstrucción

**Prompt:** Construye ejemplos del modelo estático con salarios crecientes y decrecientes tras una pequeña automatización, verificando también la factibilidad del umbral.

**Respuesta:** Se especializa la CES con $\sigma=0.8$, $\gamma(i)=e^{5i}$ y utilidad $\ln C-L^2/2$. Se resuelven oferta laboral y umbral por bisección. En 220 valores de capital se verifican las ecuaciones; los ejemplos seleccionados producen derivadas salariales aproximadas de $+0.950$ y $-1.132$. Los parámetros son ilustrativos.

## 5. Formalización — reconstrucción

**Prompt:** Formaliza un argumento verificable en Lean sin esconder conclusiones dentro de supuestos. Distingue lo probado de la traducción económica pendiente.

**Respuesta:** Se prueban tres contratos de álgebra condicional sobre el sistema de respuestas. La división exige denominador no nulo. La existencia del sistema reducido se construye explícitamente. La traducción desde la economía de tareas y la diferenciación del equilibrio quedan abiertas; no se presenta este apoyo como formalización completa de las Proposiciones 2–3.

## Evidencia de ejecución real

La carpeta `lean/` procede de esta corrida propia. El primer intento de build y su error se conservan. Tras reparar el paso algebraico, el build de `ProofInterface` y el check requerido `--fast` terminaron con código 0. `results/verification.json` contiene la salida real del programa económico. No se inventó una respuesta previa errónea de la IA: la frase absoluta sobre salarios se utiliza como hipótesis para contrastar, no como cita histórica de esta sesión.
