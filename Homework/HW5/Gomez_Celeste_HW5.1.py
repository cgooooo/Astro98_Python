#1
import numpy as np

def Equal(arr):
    equalrows = []
    for row in arr:
        if np.all(row == row[0]):
            equalrows.append(row)
    return np.array(equalrows)

arr = np.array([[1,1,1], [1,2,3], [2,2,2]])
result = Equal(arr)
print(result)
             