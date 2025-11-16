# Depressor Project Skeleton

This directory provides a structured scaffold for the Depression_New_Submit (5) experiments, aligning code, data, and documentation in one place. Use this layout to organize preprocessing, model training, evaluation, explainability, and serving workflows.

## Layout
- `requirements.txt` lists pinned runtime dependencies.
- `Makefile` offers shortcuts for environment setup, training, evaluation, and figure generation.
- `Dockerfile` captures a reproducible runtime image.
- `configs/` holds YAML configuration files for datasets, models, ensembles, and training defaults.
- `data/` separates raw sources, intermediate artifacts, processed splits, and external resources.
- `scripts/` contains command-line entrypoints for data prep, training, calibration, fusion, evaluation, significance testing, ablations, and explainability.
- `src/depressor/` is the Python package with utilities, data handling, preprocessing, models, training logic, evaluation metrics, explainability, visualization, and serving modules.
- `tests/` collects unit tests for preprocessing, stratification, metrics, thresholding, and explainability.
- `docs/` provides experiment reproduction guidance.

Refer to `docs/EXPERIMENTS.md` for instructions on reproducing tables and figures, and see the repository root README for the broader experimental outline.

## Downloadable bundle

To produce a shareable ZIP of the entire `depressor/` project (including configs, scripts, source, and docs), run:

```
make dist
```

The archive will be written to `dist/depressor.zip` with the correct directory prefix so it can be unzipped directly anywhere.
