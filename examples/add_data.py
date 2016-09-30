# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:21:24 2016

@author: daniel
"""

import matplotlib.pylab as plt
from multiplot2d import MultiPlotter
from multiplot_example_data import *

plt.close("all")
plt.ioff()

plt.close("all")
try:
    plt.style.use("dwplot")
except:
    print("Cannot use this stylesheet")

# for vector inputs,  vector shape does not matter
vector_plotter = MultiPlotter([3, 3], name="vector inputs")
vector_plotter.add_data(0, t_1d_vector, y_1d_vector, labels="1D x, 1D y")
vector_plotter.add_data(1, t_1d_vector, y_row_vector, labels="1D x, row y")
vector_plotter.add_data(2, t_1d_vector, y_col_vector, labels="1D x, col y")
vector_plotter.add_data(3, t_row_vector, y_1d_vector, labels="row x, 1D y")
vector_plotter.add_data(4, t_row_vector, y_row_vector, labels="row x, row y")
vector_plotter.add_data(5, t_row_vector, y_col_vector, labels="row x, col y")
vector_plotter.add_data(6, t_col_vector, y_1d_vector, labels="col x, 1D y")
vector_plotter.add_data(7, t_col_vector, y_row_vector, labels="col x, row y")
vector_plotter.add_data(8, t_col_vector, y_col_vector, labels="col x, col y")
vector_plotter.add_legend("all")
vector_plotter.display()

# all datasets can share a single x axis or each have their own
x_plotter = MultiPlotter(2, name="using x")
x_plotter.add_data(0, t_col_vector, y_2col_matrix, labels=["x, y1", "x, y2"])
x_plotter.add_data(1, t_2col_matrix, y_2col_matrix,
                   labels=["x1, y1", "x2, y2"])
x_plotter.add_legend(list(range(2)))
x_plotter.display()

# one plot with 9 datasets
one_nine_plotter = MultiPlotter(1, name="one plot with 9 datasets")
one_nine_plotter.add_data(0, t_col_vector, y_9col_matrix)
one_nine_plotter.display()

# 9 plots with 1 dataset each
nine_one_plotter = MultiPlotter([3, 3], name="9 plots with 1 dataset each")
nine_one_plotter.add_data("all", t_col_vector, y_9col_matrix)
nine_one_plotter.display()

# 9 plots with 9 datasets each
nine_nine_plotter = MultiPlotter([3, 3], name="9 plots with 9 datasets each")
nine_nine_plotter.add_data("all", t_col_vector, y_9col_matrix,
                           plots_share_data=True)
nine_nine_plotter.display()

# 2 plots with different datasets
two_plots_plotter = MultiPlotter(2, name="2 plots,  different datasets")
two_plots_plotter.add_data(0, t_col_vector, y_col_vector)
two_plots_plotter.add_data(1, t_col_vector, y_2col_matrix)
two_plots_plotter.add_legend(1)
two_plots_plotter.display()

# line_styles
# http://matplotlib.org/api/lines_api.html#matplotlib.lines.Line2D.set_xdata
style_plotter = MultiPlotter(2, name="style")
shared_style = dict(dict(ls="", marker="+"))
style_plotter.add_data(0, t_col_vector, y_2col_matrix,
                       line_styles=shared_style)
individual_styles = [dict(ls=":", color="g"), dict(marker="o")]
style_plotter.add_data(1, t_col_vector, y_2col_matrix,
                       line_styles=individual_styles)
style_plotter.set_plot_titles("all", ["Shared Formatting",
                                      "Individual Formatting"])
style_plotter.add_legend("all")
style_plotter.display()

plt.show()
