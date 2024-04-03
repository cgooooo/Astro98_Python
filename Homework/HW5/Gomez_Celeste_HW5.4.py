#4
import numpy as np
def sorting(matrix):
    sortedmatrix = np.sort(matrix, axis = 0)
    return sortedmatrix

np.random.seed(12345)
a = np.random.randint(1, 50, (4,5))

print('a', a)
print('sorting a', sorting(a))
