# Regression Analysis Plots with Python and Seaborn

Reusable Python scripts that fit and visualise regressions of bathymetric
depth against the observation index for the cross-section profiles of the
Mariana Trench (Pacific Ocean).

## Scripts

- `regression_5subplots.py` — linear regressions of five selected profiles
  (11–15) drawn as five panels on shared axes with the Seaborn `regplot`
  function (scatter + fitted line + confidence band). Saves `plot_RegrAn.png`.
- `regression_facetplot.py` — second-order (quadratic) regressions of all 25
  profiles as a faceted grid (five per row) with the Seaborn `lmplot`
  function; the wide table is reshaped to long form with `pandas.melt`. Saves
  `plot_FacetGrid.png`.

## Data

- `Tab-Bathy.csv` — bathymetric depths (metres) sampled at 517 observation
  points along 25 profiles across the Mariana Trench.

## Methods

Ordinary-least-squares linear and polynomial (order 2) regression with
confidence-interval estimation; small-multiple faceting; wide-to-long
reshaping (`melt`).

## Requirements

Python 3 with `pandas`, `seaborn` and `matplotlib`.

```
pip install pandas seaborn matplotlib
python regression_5subplots.py
python regression_facetplot.py
```

## Author

Polina Lemenkova — ORCID: https://orcid.org/0000-0002-5759-1089

Archived code: https://doi.org/10.13140/RG.2.2.16043.90409

## License

MIT — see the LICENSE file (Copyright Polina Lemenkova).
