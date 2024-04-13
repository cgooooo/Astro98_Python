#3
import matplotlib.pyplot as plt
import numpy as np 

def pi_est(N):
    points = np.random.uniform(0, 1, size=(N, 2))
    distance = np.sqrt(points[:, 0] ** 2 + points[:, 1] ** 2)
    inside = np.sum(distance <= 1)
    ratio = inside / N
    estimate = 4 * ratio
    return estimate

N_vals = [int(1e3), int(1e4), int(1e5), int(1e6)]

for N in N_vals:
    estimate = pi_est(N)
    print(f"Pi Estimate = {N}: {estimate}")

#plot for points for N = 1e4
N_plot = int(1e4)
points = np.random.uniform(0, 1, size=(N_plot, 2))
distance = np.sqrt(points[:, 0] ** 2 + points[:, 1] ** 2)
inside = points[distance <= 1]
outside = points[distance > 1]

plt.figure(figsize = (5,5))
plt.scatter(inside[:, 0], inside[:, 1], color = 'lightskyblue', label = 'Inside Quarter Circle')
plt. scatter(outside[:, 0], outside[:, 1], color = 'crimson', label = 'Outside Quarter Circle')
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()