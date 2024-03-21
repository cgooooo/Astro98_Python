#2.3

def oddnumslist(listA, listB):
    combolist = listA + listB
    oddnums = []

    for num in combolist:
        if num % 2 != 0:             #if a number is not divisible by 2, then it will have a remainder thats not = 0, so its odd
            oddnums.append(num)

    x = len(oddnums)
    for i in range(x-1):
        for j in range(0, x-i-1):
            if oddnums[j] > oddnums[j+1]:
                oddnums[j], oddnums[j+1] = oddnums[j+1], oddnums[j]
    return oddnums

listA = list(range(1,11))
listB = list(range(20,31))
result = oddnumslist(listA,listB)
print(result)




##Errors

#1)  def oddnumslist(listA, listB)                                 ^
#SyntaxError: expected ':'
### added colon
            
#2)  of oddnums[j] > oddnums[j+1]:
#SyntaxError: invalid syntax
### bruh i put of instead of if

#3)  oddnums[j], oddnums[j+1] = oddnums[j+1], oddnums[j]
#    ^
#IndentationError: expected an indented block after 'if' statement on line 13
###indented line one more tab over

#4)  combolist = [listA + ListB]
#                         ^^^^^
#NameError: name 'ListB' is not defined. Did you mean: 'listB'?
###removed capitalization

#5) oddnums = [num]
#               ^^^
#UnboundLocalError: cannot access local variable 'num' where it is not associated with a value
### little confused here but i just deleted the num and am trying to leave an empty set