#!/usr/bin/env python
# coding: utf-8
"""Regression analysis - faceted plot (Seaborn lmplot).

Reshapes the Mariana Trench bathymetry into long format and draws a grid of
second-order (quadratic) regression fits of depth against observation index,
one facet per cross-section profile (25 facets, five per row). Each facet
shows the jittered scatter of depths with the fitted polynomial trend.

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

sb.set_theme(style='darkgrid', font_scale=3)

dfM = pd.read_csv(os.path.join(HERE, 'Tab-Bathy.csv'))

# reshape the wide profile columns (profile1 ... profile25) into long form
profiles_list = [f'profile{i}' for i in range(1, 26)]
df = dfM.melt(id_vars=['observ'], value_vars=profiles_list,
              var_name='Profiles', value_name='Depths')

g = sb.lmplot(data=df, x='observ', y='Depths',
              col='Profiles', hue='Profiles', col_wrap=5,
              fit_reg=True, truncate=True,
              x_jitter=True, y_jitter=True,
              scatter=True, markers='.', order=2, height=6)
g.set_axis_labels('Observation points', 'Depths, m')
g.fig.subplots_adjust(wspace=0.04)

plt.tight_layout()
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95,
                    hspace=0.25, wspace=0.35)
plt.savefig(os.path.join(HERE, 'plot_FacetGrid.png'), dpi=300)
plt.show()
