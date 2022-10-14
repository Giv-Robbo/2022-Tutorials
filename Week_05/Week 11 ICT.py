"""
Created on Wed Oct 12 13:06:03 2022

@author: Giv

Week Eleven ICT
"""

import numpy as np
import matplotlib.pyplot as plt

w, h = 5, 4

T = np.zeros(20)
bottom_boundary = np.array([110,100,90,80,70]) + 273.15
i = 0
j = np.arange(0,w)
s = i*w + j
T[s] = bottom_boundary

top_boundary = np.array([0,10,20,30,40]) + 273.15
i = h-1
j = np.arange(0,w)
s = i*w + j
T[s] = top_boundary

left_boundary = np.array([110,65,25,0]) + 273.15
j = 0
i = np.arange(0,h)
s = i*w + j
T[s] = left_boundary

right_boundary = np.array([70,60,50,40]) + 273.15
j = w-1
i = np.arange(0,h)
s = i*w + j
T[s] = right_boundary

print(T)
plt.matshow(T.reshape((h,w)), origin = "lower")

# for i in range(h):
#     #Left and Right
#     j = 0
#     s = i*w + j
#     T[s] = 110 + 273.15 #Kelvin
#Set up initial conditions later

k = 54
rho = 7860
Cp = 490
dt = 1
dx = 0.025

sigma = k/(rho*Cp) * dt / (dx**2)
print(sigma)

M = np.zeros((20,20))
for i in range(h): #Row
    for j in range(w): #Column
        s = i*w + j
        
        #Bottom
        if i == 0:
            M[s,s] = 1
            continue
        #Top
        if i == h-1:
            M[s,s] = 1 
            continue
        #Left
        if j == 0:
            M[s,s] = 1
            continue
        #Right
        if i == w-1:
            M[s,s] = 1 
            continue
        
        #Horizontal derivative (d^2T/dx^2)
        M[s, s-1] += -1 * sigma
        M[s, s] += 2 * sigma
        M[s, s+1] += -1 * sigma
        
        
        #Vertical derivative (d^2T/dy^2)
        M[s, s-w] += -1 * sigma
        M[s, s] += 2 * sigma
        M[s, s+w] += -1 * sigma
        
        #One side of time derivative
        M[s,s] += 1
        
fig, ax = plt.subplots()
ax.matshow(M)
plt.show()

for _ in range(5):
    T_new = np.linalg.solve(M,T)
    T = T_new
    
fig, ax = plt.subplots()
ax.matshow(T.reshape((h,w)), origin = 'lower')
plt.show()
