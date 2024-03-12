#Write a function that takes a list of numbers as input and returns 
#the mini-mum and maximum values in the list as a tuple.

def min_max(i):

    minval = maxval = i[0] #0 starts the first number of the list
    for num in i:
        if num < minval:
            minval = num 
        if num > maxval:
            maxval = num
    return (minval, maxval)

myList = [19,33,2,20,10,56,104,2]
result = min_max(myList)
print(result)

