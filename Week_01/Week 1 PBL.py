"""
Created on Fri Jul 29 13:15:18 2022

@author: Giv

Week 1 PBL
"""
import numpy as np
from matplotlib import pyplot as plt

#Constants
L = 0.01 #length, m
d = 5e-6 #diameter, m
k = 200 #thermal conductivity, W/mK
h_bar = 1000 #heat transfer coeff, W/m2K
Ta = 293.15 #ambient temp, K
T0 = 353.15 #left side temp, K
T4 = 343.15 #right side temp, K
n = 5 #number of nodes

P = np.pi*d
A = np.pi*(d**2)/4
dx = L/n
beta_sq = (h_bar*P)/(k*A)
sigma = -2-beta_sq*(dx**2)

def matrix_m(n, sigma):
    a = np.diag(np.ones(n-1),-1)
    b = np.diag(np.ones(n)*sigma)
    c = np.diag(np.ones(n-1),1)
    d = a+b+c
    d[0][0] = 1
    d[n-1][n-1] = 1
    return d

def solv_temp(sigma,n,T0,Ta,T4):
    b = np.zeros((n,1))
    b[0] = T0 - Ta
    b[n-1] = T4 - Ta
    m = matrix_m(n,sigma)
    return np.linalg.solve(m,b)
    

def analytical_sol(beta,x,L,sigma_L,sigma_0):    
    return (sigma_L*np.sinh(beta*x) + sigma_0*np.sinh(beta*(L-x)))/np.sinh(beta*L)
    
answ = solv_temp(sigma,n,T0,Ta,T4)
print(answ)

def x_array(n,L):
    x = 0
    dx = L/(n-1)
    tup = []
    for i in range(n):
        tup.append(x)
        x += dx
    return tup

analy_sol = []
for i in x_array(n,L):
    analy_sol.append(analytical_sol(beta_sq**0.5,i,L,T4,T0))
    
print(analy_sol)

#plt.plot(answ,x_array(n,L))                 
                  