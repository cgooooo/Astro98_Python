#2.2
def square(list):
    squaredlist = [x ** 2  for x in list]
    return squaredlist

lis = [2, 3, 4]
print(square(lis))

#Errors

# 1) tried printing and got <function square at 0x1005485e0>.
### took x out of def square(x):

# 2) line 3, in square
#   squaredlist = [x ** 2  for x in list]
#TypeError: 'type' object is not iterable
### changed print(square(list)) to print(square(lis))

