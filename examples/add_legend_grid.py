# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 13:02:31 2016

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

basic_plotter=MultiPlotter(1,size_inches=[6,3],name="legend and grid with no options")
basic_plotter.add_data(0,t_col_vector,y_2col_matrix,labels=["data 1", "data 2"])
basic_plotter.add_legend(0)
basic_plotter.add_grid(0)
basic_plotter.display()

# legend args: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend
# grid args: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.grid
options_plotter=MultiPlotter(1,size_inches=[6,3],name="legend and grid with some options")
options_plotter.add_data(0,t_col_vector,y_2col_matrix,labels=["data 1", "data 2"])
legend_style=dict(loc="best", title="My Legend")
options_plotter.add_legend(0,legend_args=legend_style)
grid_style=dict(ls="dashed")
options_plotter.add_grid(0,grid_args=grid_style)
options_plotter.display()