# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 13:13:53 2022

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt

# Pandas for more complex data-loader
x, f = np.loadtxt("data_points.txt", unpack = True)
data = np.column_stack((x,f))

##np.savetxt("output_file.txt", data, fmt='%4F')

#Question 1
#P.T * P * X = P.T * f

#Turn into column vector
X = np.atleast_2d(x).T
F = np.atleast_2d(f).T

#P = [p0, p1, p2]
p0 = x**0
p1 = x**1
p2 = x**2

P = np.column_stack((p0,p1,p2))

a = np.linalg.inv(P.T @ P) @ P.T @ F

smooth_x = np.linspace(0,3)
fitted_trend = a[0] + a[1] *smooth_x + a[2] * smooth_x**2
fig, ax = plt.subplots()

#ax.scatter(x,f)
#ax.plot(smooth_x,fitted_trend,'r')
#plt.show()

#Question 2
def f(x):
    return x*(np.pi - x)

def f_approx(x):
    return (8/np.pi)*np.sin(x) + (8/27*np.pi)*np.sin(3*x)

#ax.scatter(smooth_x, f(smooth_x))
#ax.plot(smooth_x,f_approx(smooth_x),'r')
#plt.show

#Question 3
