#For both minimum and maximum, write one function to manually find that
#value using a for loop and another to manually find it using a while loop. You
#may not use min() or max(). In total you should have written 4 functions

#FOR LOOPS
def formin(n):
    minval = n[0]
    for num in n:
        if num < minval:
            minval = num
    return minval
    
def formax(n):
    maxval = n[0]
    for num in n:
        if num > maxval:
            maxval = num 
    return maxval

#WHILE LOOPS
def whilemin(n):
    minval = n[0]
    i = 1
    while i < len(n):
        if n[i] < minval:
            minval = n[i]
        i += 1
        return minval
        

def whilemax(n):
    maxval = n[0]
    i = 1
    while i < len(n):
        if n[i] > maxval:
            maxval = n[i]
        i += 1
    return maxval


myList = [2,4,6,8]

result1 = formin(myList)
result2 = formax(myList)
result3 = whilemin(myList)
result4 = whilemax(myList)


print('For Loop Min', result1)
print('For Loop Max', result2)
print('While Loop Min', result3)
print('While Loop Max', result4)