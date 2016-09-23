# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 17:24:00 2016

@author: daniel
"""

import numpy as np

f=np.sin

t_1d_vector = np.arange(0,20,0.1)

t_len=np.size(t_1d_vector)

t_row_vector = np.array([t_1d_vector])
t_col_vector = t_row_vector.T
t_2col_matrix = np.column_stack((t_col_vector,t_col_vector))

y_1d_vector = f(t_1d_vector)
y_row_vector = f(t_row_vector)
y_col_vector = f(t_col_vector)
y_2col_matrix = np.zeros((t_len,2))
y_2col_matrix[:,0:1] = f(y_col_vector)
y_2col_matrix[:,1:2] = 2*f(y_col_vector)+2

y_3col_matrix=np.zeros((t_len,3))
for col in range(3):
    y_3col_matrix[:,col:col+1]=(col+1)*f(t_col_vector)+col

noise=np.random.normal(0,0.2,np.shape(y_3col_matrix))
y_3col_noise_matrix=y_3col_matrix+noise

y_9col_matrix=np.zeros((t_len,9))
for col in range(9):
    y_9col_matrix[:,col:col+1]=(col+1)*col*f(t_col_vector)+col
