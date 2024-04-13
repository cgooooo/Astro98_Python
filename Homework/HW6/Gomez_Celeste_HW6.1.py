#1
import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(40)
data1 = np.random.randint(0, 101, 40)
data2 = np.random.randint(0, 101, 40)
data3 = np.random.randint(0, 101, 40)

plt.figure()

plt.subplot(2, 1, 1)
plt.plot(range(len(data1)), data1, color = 'peachpuff', linewidth = 10)
plt.plot(range(len(data2)), data2, color = 'crimson', linestyle = '--')

plt.subplot(2,1,2)
plt.scatter(range(len(data3)), data3, color = 'magenta', marker = 'D')

plt.show()