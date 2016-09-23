# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 13:26:09 2016

@author: daniel
"""

import matplotlib.pylab as plt
from multiplot2d import MultiPlotter
from multiplot_example_data import *

plt.close("all")
plt.ioff()

plt.close("all")
try: plt.style.use("dwplot")
except: print "Cannot use this stylesheet"

# some formatting
measure_style=dict(ls="",marker="o",markersize=5)
legend_args=dict(loc='upper center',ncol=2,fontsize='medium')

compare_col=MultiPlotter([3,1],size_inches=(5,5),name="Model vs. Data")
compare_col.add_data("all",t_col_vector,y_3col_noise_matrix,line_styles=measure_style,labels="Data")
compare_col.add_data("all",t_col_vector,y_3col_matrix,labels="Model")
# add a figure legend (as opposed to plot legend)
compare_col.add_figure_legend(legend_args,0.3)
compare_col.display()

compare_row=MultiPlotter([1,3],size_inches=(7,5/3.),name="Model vs. Data")
compare_row.add_data("all",t_col_vector,y_3col_noise_matrix,line_styles=measure_style,labels="Data")
compare_row.add_data("all",t_col_vector,y_3col_matrix,labels="Model")
# add a figure legend (as opposed to plot legend)
compare_row.add_figure_legend(legend_args,0.3)
compare_row.display()