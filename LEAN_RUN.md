# Corrida propia y alcance de Lean

La formalización empezó desde la raíz de un clon nuevo de AppliedModelingLib, revisión `2db7d108cd3a2cb10148974bb2a77856e7d87428`, mediante el agente configurado como **GPT-6 Astra (`gpt-6-astra`), razonamiento `high`**, por decisión expresa del usuario. Esta configuración sustituye la recomendación de GPT-5.6 Sol xhigh de la consigna. El agente principal reanudó la validación tras el restablecimiento del saldo.

Fuente: NBER 22252, junio de 2017, 87 páginas; hash y URL en `sources.md` y `lean/audit/source_provenance.json`. Se generó `papers/AR18RaceManMachine/` mediante la entrada oficial `paper_contribution.py new`. Solo se reutilizó la caché de dependencias del trabajo anterior; ninguna formalización de otro paper fue copiada como resultado propio.

## Resultados efectivamente comprobados

| Contrato | Contenido | Límite |
|---|---|---|
| `StaticResponseAlgebraSpec` | Resuelve las respuestas de salario, renta y empleo a partir de tres ecuaciones linealizadas | No deriva las ecuaciones de la economía continua |
| `StaticResponseExistenceSpec` | Construye una solución del sistema reducido cuando el denominador no es cero | No demuestra existencia del equilibrio económico original |
| `WageDeclinePossibleAlgebraSpec` | Construye productividad positiva con respuesta salarial negativa | No construye por sí solo parámetros factibles de la economía no lineal |

`MainTheorems.lean` contiene las pruebas; `PaperInterface.lean` contiene Specs transparentes; `ProofInterface.lean` enlaza cada Spec con su prueba exacta. Son tres resultados de apoyo, **no tres proposiciones del paper formalizadas**. El ejemplo numérico aporta evidencia separada de factibilidad de ambos signos; no reemplaza el puente formal ausente.

La primera compilación falló en dos pasos de álgebra. Tras reescribir con la identidad de respuesta relativa, la compilación específica terminó correctamente. Se conserva el primer diagnóstico.

| Comando | Resultado |
|---|---|
| `lake build +AR18RaceManMachine.ProofInterface` | Código **0**, build exitoso |
| `python3 scripts/paper_contribution.py check AR18RaceManMachine --fast` | Código **0**, interfaz y comprobación rápida exitosas |

Salidas literales: `lean/audit/narrow-build-final.txt` y `lean/audit/fast-check.txt`; códigos en `lean/audit/check_results.json`. En Windows se utilizó el adaptador externo que proporciona `fcntl` mediante bloqueos `msvcrt` y compatibilidad `os.fchmod`. Ese adaptador ejecuta el mismo módulo `scripts.paper_contribution`; no se cambiaron sus validaciones. El soporte reproducible se conserva fuera de la copia en `reproducibility/`.

## Qué no está probado

La comprobación rápida **no equivale al cierre completo de AppliedModelingLib**. No están terminados el inventario independiente, la fijación formal de todo el mapa de fuente, la revisión semántica ni el cierre adversarial. Permanecen abiertos los resultados originales del paper: equilibrio continuo, diferenciación, productividad, acumulación de capital, BGP, innovación endógena, desigualdad y bienestar. El archivo de auditoría de fuente conserva su estado pendiente; no se inventó una aprobación.

Hubo una interrupción por límite de uso durante la sesión inicial. Este no es el resultado final del componente: tras reanudar, **el build y el check rápido terminaron con código 0**. Lo parcial es la cobertura matemática y semántica descrita arriba.

## Copia íntegra

La carpeta completa generada se copia byte a byte de `papers/AR18RaceManMachine/` a `lean/`, sin seleccionar, renombrar ni reescribir sus archivos durante la copia. `logs/lean-copy.json` registra hashes y comparación. Los ajustes de estado se hicieron dentro de la corrida original antes de congelar y copiar.

Se usa `git add lean/` ordinario. Se respetan el `.gitignore` generado y las exclusiones de fuentes del repositorio origen; los PDF y el texto completo del paper quedan locales e ignorados. No se emplea `git add -f`. La copia completa está localmente disponible, aunque esos bytes fuente no se publican.
