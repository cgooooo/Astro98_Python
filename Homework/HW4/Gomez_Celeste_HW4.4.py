#4

def removedupes(list):
    newlist = []

    for x in list:
        if x not in newlist:
            newlist.append(x)

    return(newlist)

list = [2,4,5,5,5,6,7,3,1,2,2,3,2,4,2,1,0,9,7,7,5,3,5,7]
result = removedupes(list)
print(result)


##ERRORS

#1) line 8
#    return newlist
#SyntaxError: 'return' outside function
### erm where did my parentheses go?? added parentheses

#3) Cell In[8], line 3
#----> 3 for num in list:
#TypeError: 'type' object is not iterable
### tried changing num to x, then to item but i still kept getting the same 


#4) same error as 1
###i coulndt figure out what it meant so i just kept either changing parentheses or putting more lines in between
### TURNS OUT IT WAS AN INDENT PROBLEM
###ALL THE HOMIES HATE INDENT PROBLEMS

