#2
import matplotlib.pyplot as plt
import numpy as np 

a = 16.02
b = 0.1124
R = 0.083144

pressure = np.linspace(1, 10, 100)
volume = np.linspace(1, 30, 100)

P, V = np.meshgrid(pressure, volume) #meshgrid just combines the 1D arrays into a rectangualr grid
T = (P + a / (V ** 2)) * (V - b) / R

plt.figure()
plt.pcolormesh(P, V, T, cmap = 'PuRd', vmin = np.min(T), vmax = np.max(T))
plt.xlabel('Pressure')
plt.ylabel('Volume (L)')

plt.colorbar(label = 'Temperature (K)')
plt.show()
