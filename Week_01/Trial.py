"""
Created on Wed Jul 27 13:25:00 2022

@author: Giv

Exercise 1 from week 1 ICT1
"""
import numpy as np

def f1(x):
    return x**3

def f2(x):
    return 3*x**2-2*x

def f3(x):
    return np.sin(x)
    
def forward_diff(f,x,h):
    return (f(x+h)-f(x))/h

x=np.array([-5,-4,5])
h=np.array([0.1,0.0001,0.0001])
