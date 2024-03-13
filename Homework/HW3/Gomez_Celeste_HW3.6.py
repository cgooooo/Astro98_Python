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


myList = [10,88,3,10,4,104]

result1 = formin(myList)
result2 = formax(myList)
result3 = whilemin(myList)
result4 = whilemax(myList)
print(result1, result2, result3, result4)