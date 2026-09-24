# Reproducción

## Economía

Con Python 3.12 o posterior, desde la raíz:

```bash
python -m pip install -r requirements.txt
python analysis/static_model.py
```

Se generan `results/verification.json`, el barrido CSV y las figuras PDF/PNG. No hay semilla aleatoria: el cálculo es determinista. Se utiliza bisección con raíces acotadas y tolerancia explícita. Se sustituyó SciPy porque Windows bloqueó una DLL; no se desactivó ninguna protección del equipo.

## Presentación

```bash
tectonic -k --keep-logs presentation.tex
```

Se utilizó Tectonic 0.17.0. También puede compilarse con una distribución LaTeX y los paquetes del preámbulo. La presentación tiene 17 diapositivas principales y dos páginas de apéndice, sin animaciones. Las fotos originales están en `hand/derivacion-01.jpg` y `hand/derivacion-02.jpg`. El Beamer incorpora detalles ampliados y las páginas completas; recompilar conserva esa disposición.

## Lean

Clonar AppliedModelingLib y seleccionar la revisión indicada en `sources.md`. Instalar la versión de `lean-toolchain` y las dependencias fijadas por `lake-manifest.json`. Copiar íntegra `lean/` a `papers/AR18RaceManMachine/`. Copiar `reproducibility/AR18RaceManMachine.lean` a `papers/AR18RaceManMachine.lean` y añadir el bloque de `reproducibility/lake-target.toml` al `lakefile.toml`, solo si ese target no existe.

```bash
lake exe cache get
lake build +AR18RaceManMachine.ProofInterface
python3 scripts/paper_contribution.py check AR18RaceManMachine --fast
```

No ejecutar `lake build` en la raíz de este repositorio semanal: `lean/` conserva la organización de un paper de AppliedModelingLib, no es un proyecto Lean independiente. En Windows, los adaptadores conservados en `reproducibility/python-compat/` pueden ser necesarios; consultar `LEAN_RUN.md`. Un build exitoso no cierra las revisiones semánticas pendientes.
