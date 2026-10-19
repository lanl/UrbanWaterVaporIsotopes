# Urban Water Vapor Isotopes

This repository contains the data and code required to reproduce the analyses,
figures, tables, and reviewer-validation checks for:

**"Isotopic Evidence for Modification of Column Water Vapor by Cities"** (2026)  
Martin Velez Pardo, David C. Noone, and Richard P. Fiorella  
Submitted to *Nature Communications*.

## Repository contents

- `UrbanWaterVaporIsotopes.ipynb` — main reproducibility notebook
- `environment.yml` — Conda environment used to reproduce the analysis
- `source_data/` — archived input datasets required by the notebook
- `source_data/natural_earth/` — local Natural Earth 10m river/lake shapefiles
  used for map context
- `assets/` — static publication assets, including the Figure 3 schematic
- `output/figures/` — numbered manuscript/supplementary figures and additional
  validation figures
- `output/tables/` — numbered manuscript/supplementary tables and supporting
  diagnostic/provenance files
- `output/cache/` — optional regenerable computational caches
- `SHA256SUMS.txt` — SHA-256 checksums for the archived repository files

## Reproducibility design

The notebook is organized as a single public workflow with shared setup/path
definitions followed by figure, table, and validation sections.

- All paths are relative to the repository root.
- The analysis uses the native **0.05 degree** TROPOMI climatology grid.
- Numbered publication outputs are written to `output/figures/` and
  `output/tables/`.
- Reviewer/validation diagnostics that informed the revision are retained and
  clearly distinguished from numbered publication outputs.
- Figure 3 is a static conceptual schematic and is archived in `assets/`.
- Computational caches are optional. Deleting `output/cache/` may make a rerun
  slower but should not change the analysis.

During archive preparation, the notebook was successfully run from an empty
cache, confirming that the retained source data are sufficient to regenerate
the computational outputs. The release archive is therefore intended to be
distributed without precomputed cache files.

## TROPOMI climatology

The archived TROPOMI file is:

`source_data/TROPOMI_HDO_CLEAR_p05_quadratic_climatology.nc`

It is a **losslessly compressed variable subset** of the full analysis
climatology. Only variables required by the analyses in this repository are
retained. The decoded values of every retained variable were verified to be
identical to those in the original full climatology.

This keeps the public archive substantially smaller while preserving the
scientific inputs used by the notebook exactly.

## Other archived inputs

The notebook also uses the following repository inputs where relevant:

- `PercentSettlementArea_regridded_to_TROPOMI_quadratic_climatology_0p05.nc`
- `ETOPO_2022_v1_30s_N90W180_surface_resampled_to_TROPOMI_quadratic_climatology_p05.tif`
- `landseamask_regridded_to_TROPOMI_quadratic_climatology_0p05_nearest.nc`
- `MCD12C1_IGBP_broad_climatology_2017-2024_TROPOMIgrid.nc`
- `MCD12C1_IGBP_detailed_climatology_2017-2024_TROPOMIgrid.nc`
- `cities15000.txt`
- `top400_cities.csv`
- `top2000_cities.csv`
- `SameDay_daily_only_city_days.csv`

The city-map sections also use four Natural Earth 10m shapefile families stored
locally under `source_data/natural_earth/`:

- `ne_10m_rivers_lake_centerlines.*`
- `ne_10m_rivers_lake_centerlines_scale_rank.*`
- `ne_10m_lakes.*`
- `ne_10m_lakes_north_america.*`

The notebook reads these files locally and does not require downloading Natural
Earth data at runtime.

For provenance and citations of the underlying observational and ancillary
datasets, see the associated manuscript and Supplementary Information.

## Software environment

A validated Conda environment is provided in `environment.yml`. The main
scientific package versions are pinned to the versions used in the successful
analysis environment; small notebook/runtime dependencies are left for Conda
to resolve compatibly.

Create the environment from the repository root with:

```bash
conda env create -f environment.yml
conda activate urban-water-vapor-isotopes
```

If desired, register it as a Jupyter kernel:

```bash
python -m ipykernel install --user \
  --name urban-water-vapor-isotopes \
  --display-name "Python (Urban Water Vapor Isotopes)"
```

Then launch Jupyter from the **repository root**:

```bash
jupyter lab
```

and open:

`UrbanWaterVaporIsotopes.ipynb`

Launching from the repository root is important because the notebook defines
its project root with `Path.cwd()`.

## Running the notebook

For a complete reproduction:

1. Create and activate the Conda environment.
2. Launch Jupyter from the repository root.
3. Select the `urban-water-vapor-isotopes` kernel.
4. Restart the kernel.
5. Run the notebook from top to bottom.

The setup cell defines the shared repository paths and should always be run
before individual analysis sections. Several later sections intentionally reuse
outputs produced earlier in the notebook, particularly the per-city-season
results from Figure 2.

Some model, bootstrap, regional-matching, and sensitivity sections are
computationally intensive. The notebook may create files under `output/cache/`
to accelerate repeated execution. These are not required source data.

## Publication outputs

The notebook generates the numbered publication outputs:

- Main Figures 1-4
- Main Tables 1-2
- Supplementary Figures 1-9
- Supplementary Tables 1-7

PNG and PDF versions of numbered figures are written to `output/figures/`.
Tabular publication outputs and their supporting machine-readable files are
written to `output/tables/`.

Additional unnumbered files in `output/figures/` and `output/tables/` document
robustness tests, intermediate summaries, reviewer-validation analyses, and
provenance. Examples include model-consistency diagnostics, threshold
sensitivity, sampling diagnostics, same-day tests, interannual recurrence, and
the optional median-based regional robustness check.

## Figure 3

Figure 3 is a conceptual schematic rather than a programmatically generated
analysis figure. Its source files are archived as:

- `assets/Figure_3_Two_layer_model.pdf`
- `assets/Figure_3_Two_layer_model.png`

Copies may also appear in `output/figures/` for a complete numbered output set.

## Computational caches

Files under `output/cache/` are optional and regenerable. They are used only to
speed up expensive repeated computations.

The archived release should contain no precomputed cache contents other than an
optional `.gitkeep` placeholder. To clear caches safely from the repository
root:

```bash
find output/cache -mindepth 1 -maxdepth 1 ! -name '.gitkeep' -exec rm -rf {} +
```

A successful clean-cache run was completed during archive preparation; a second
full run is not required solely because caches are removed afterward.

## File integrity

`SHA256SUMS.txt` contains SHA-256 checksums for the archived files, excluding
the checksum file itself, version-control metadata, notebook checkpoints, and
the regenerable `output/cache/` directory.

On macOS, checksums can be verified from the repository root with:

```bash
shasum -a 256 -c SHA256SUMS.txt
```

On systems with GNU coreutils:

```bash
sha256sum -c SHA256SUMS.txt
```

## Data and code availability

This repository is intended for archival release with the associated
publication. The final Zenodo DOI and repository citation should be added here
after deposit.

**Zenodo DOI:** to be added after deposit.

## LANL software release and licensing

**Approved software title:** UrbanWaterVaporIsotopes

**LANL software release approval:** O5230

This software was developed at Los Alamos National Laboratory
and approved for open-source distribution under release O5230.

Copyright © 2026. Triad National Security, LLC.
All rights reserved.

This program is open-source under the BSD-3-Clause License.
See [LICENSE](LICENSE) for the complete copyright notice,
license conditions, and disclaimer.

**Source code:**
https://github.com/LANL/UrbanWaterVaporIsotopes

