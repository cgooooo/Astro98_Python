#3
import numpy as np

def spaceBetween(arr):
    result = []
    for word in range(len(myarr)):
        result.append(' '.join(myarr[word]))
    return result

myarr = np.array(['my', 'dog', 'likes', 'to', 'fart'])
result = spaceBetween(myarr)
print(result)
    