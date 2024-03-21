#3.2

biglist = [[0 for x in range(5)] for x in range(5)]

num = 1
for i in range(5):
    for j in range(5):
        biglist[i][j] = num
        num += 1
        
biglist = []

num = 1
for i in range(5):
    row = []
    for j in range(5):
        if num % 3 == 0:
            row.append('?')
        else:
            row.append(num)
        num += 1
    biglist.append(row)


for i in range(5):
    print(biglist[i])




##Errors
    
#1) name 'append' is not defined
### I had typed append.row each time i was trying to append but they were supposed to be swapped
    
#2) Cell In[5], line 12
#    else:
#    ^
#SyntaxError: invalid syntax
### i think the indent was too far. i moved it an indnent back and it seemed to work
    
#3) Cell In[6], line 19
#---> 19 for i in range(5) in biglist:
#TypeError: 'bool' object is not iterable
###got rid of "in biglist" and just left it as for i in range(5)