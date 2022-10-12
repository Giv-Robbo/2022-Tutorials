"""
Created on Wed Aug 31 13:22:13 2022

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, rfft, fftshift, dst

x_data = np.linspace(0, np.pi, 200)
y = dst(x_data)
# fig, ax = plt.subplots()
# ax = plt.plot(y)
plt.plot(x_data,y)