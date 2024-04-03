#2
def checkerboard():
    arr = np.empty((8,8))
    
    arr[::2, ::2] = 0
    arr[1::2, 1::2] = 0
    arr[1::2, ::2] = 0
    arr[::2, 1::2] = 1
    return arr
result = checkerboard()
print(result)