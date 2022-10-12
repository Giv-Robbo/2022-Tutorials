"""
Created on Fri Sep 16 14:16:29 2022

@author: Giv
"""

import numpy as np
import matplotlib as plt

n = 100
P0 = 5 #atm
k = 1*10**-14 #m2
mu = 1*10**6 #Pa.s
c = 1*10**-8 #1/Pa
phi = 0.3 #%
bc = 2 #atm
L = 1

def pipe_pressure(P0, k, mu, c, phi, bc, L, n):
    #Dh = k/(phi*mu*c)
    #dt = 0.5*(dx**2)/Dh
    dx = L/n
    sigma = 0.5
    
    #Setting up the matrix 
    Matrix_dia = np.diag(np.ones((n,n))*(1-2*sigma))
    Matrix_low = np.diag(np.ones((n,n))*sigma,-1)
    Matrix_up = np.diag(np.ones((n,n))*sigma, 1)
    sig_matr = Matrix_dia + Matrix_low + Matrix_up
    sig_matr[0][0] = P0
    sig_matr[n][n] = bc
    
    #Initial Pressure Condition
    P = np.ones((n,n))*P0
    P[-1] = bc
    
    error = 1
    while error > 10*-6:
        P_new = np.matmul(sig_matr, P)
        for i in n:
            if abs(P[n]-P_new[n]) > error:
                error = abs(P[n]-P_new[n])
        P = P_new
    
    return P_new, dx

P, dx = pipe_pressure(P0, k, mu, c, phi, bc, L, n)
x = np.linspace(0,L,dx)
plt.plot(x,P)
plt.xaxis("Distance along Pipe, m")
plt.yaxis("Pressure, atm")
plt.title("Pressure Distribution")
plt.show()
