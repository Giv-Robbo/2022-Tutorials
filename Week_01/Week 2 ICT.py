"""
Created on Wed Aug  3 13:03:44 2022

@author: Giv

Week 2 ICT
"""
import numpy as np
import matplotlib.pyplot as plt

def fact(n):
    #Return n!
    output = 1
    for term in range(1,n+1):
        output *= term
    return output

def exptaylor(n,x):
    #Return Taylor Series of exp(x) using n terms
    #exp(x) = 1 + x + x**2/2 + ...
    #       = 1/0! + x/1! + x**2/2!
    output = 0
    for term in range(0, n+1):
        # output += 1/fact(term) * x**term
        suboutput = 1
        for subterm in range(1, n+1):
            suboutput *= subterm
        output += 1/suboutput * x**term   
    return 

def better_exp(n,x):
    #Return taylor series of exp(x) using n terms
    term = 1 #0th term
    output = term
    for i in range(1, n+1):
        term *= x/i
        output += term
    return output

#Q3      
#x_axis = np.arange(-2,1,0.1)
#y_axis = np.exp(x_axis)

#fig, ax = plt.subplots()
#ax.plot(x_axis, y_axis)

#Q4
x_axis = np.arange(-2,2,0.1)
y_axis = np.exp(x_axis)
y_axis2 = better_exp(2, x_axis)

fig, ax = plt.subplots()
ax.plot(x_axis, y_axis)
ax.plot(x_axis, y_axis2)