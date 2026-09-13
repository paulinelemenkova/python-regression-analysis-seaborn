#!/usr/bin/env python
# coding: utf-8
"""Regression analysis - five-panel plot (Seaborn regplot).

Fits and draws linear regressions of bathymetric depth against the
observation index for five selected cross-section profiles (11-15) of the
Mariana Trench, one panel each, on shared axes. Every panel shows the
scatter of depths with the fitted regression line and its confidence band.

Data:    Tab-Bathy.csv - bathymetric depths sampled at 517 observation
         points along 25 profiles across the Mariana Trench.

Author:  Polina Lemenkova
ORCID:   https://orcid.org/0000-0002-5759-1089
Archive: https://doi.org/10.13140/RG.2.2.16043.90409
License: MIT
"""
import os

import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

sb.set_style('darkgrid')
sb.set_context('paper')

df = pd.read_csv(os.path.join(HERE, 'Tab-Bathy.csv'))

fig, ax = plt.subplots(1, 5, sharex=True, sharey=True,
                       figsize=(10.0, 4.0), dpi=300)
fig.suptitle('Regression analysis plot: Mariana Trench bathymetry',
             fontsize=10, fontweight='bold', x=0.5, y=0.97)
sb.regplot(x='observ', y='profile11', data=df, marker='.', ax=ax[0])
sb.regplot(x='observ', y='profile12', data=df, marker='.', ax=ax[1])
sb.regplot(x='observ', y='profile13', data=df, marker='.', ax=ax[2])
sb.regplot(x='observ', y='profile14', data=df, marker='.', ax=ax[3])
sb.regplot(x='observ', y='profile15', data=df, marker='.', ax=ax[4])

plt.tight_layout()
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95,
                    hspace=0.25, wspace=0.35)
plt.savefig(os.path.join(HERE, 'plot_RegrAn.png'), dpi=300)
plt.show()
