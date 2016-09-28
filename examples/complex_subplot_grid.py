# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 17:22:37 2016

@author: daniel
"""

from multiplot2d import MultiPlotter
from multiplot_example_data import *
import matplotlib.pylab as plt
import matplotlib.gridspec as gridspec

plt.ioff()
plt.close("all")

################
# subplot2grid #
################

plt.figure()
ax_list = []
ax_list.append(plt.subplot2grid((3, 3), (0, 0), colspan=3))
ax_list.append(plt.subplot2grid((3, 3), (1, 0), colspan=2))
ax_list.append(plt.subplot2grid((3, 3), (1, 2), rowspan=2))
ax_list.append(plt.subplot2grid((3, 3), (2, 0)))
ax_list.append(plt.subplot2grid((3, 3), (2, 1)))

sp2g_plotter = MultiPlotter(ax_list, name="subplot2grid fig")
sp2g_plotter.add_data("all", t_col_vector, y_2col_matrix)
sp2g_plotter.display()

############
# gridspec #
############

plt.figure()
ax_list = []
gs = gridspec.GridSpec(3, 3)
ax_list.append(plt.subplot(gs[0, :]))
ax_list.append(plt.subplot(gs[1, :-1]))
ax_list.append(plt.subplot(gs[1:, -1]))
ax_list.append(plt.subplot(gs[-1, 0]))
ax_list.append(plt.subplot(gs[-1, -2]))

gs_plotter = MultiPlotter(ax_list, name="gridspec fig")
test = gs_plotter.add_data("all", t_col_vector, y_2col_matrix)

# modify gridspec subplots
# they are passed as reference to MultiPlotter, so you can still edit them
# however, MultiPlotter.display() runs plt.tight_layout, which is not
# compatible with
# subplots that were modified with gs.update()
# you will get a warning if gs.update() is used
# uncomment the next line to see what happens

# gs.update(left=0.05, right=0.8, wspace=0.05)

gs_plotter.display()

plt.show()
