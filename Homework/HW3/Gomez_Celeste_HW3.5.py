#Implement a function called rotate digits that takes an integer n as input
#and rotates its digits to the right by one position. For example, given the
#input 12345, the function should return 51234. You may *not* convert the
#input to a string but you can use properties of a string in your answer.
#Hint: Use modulus (%) and floor division (//).
#Ex: 12345 % 10 = 5 and 12345 // 10 = 1234

def rotatedigits(n):
    lastdigit = n % 10                          #modulus to find last digit
    otherdigits = n // 10                       #floordiv to truncate the last dogit
    tenpower = 1                                #multiplying by 10 until last digit > otherdigits to put it on the furthest left 
    while tenpower <= otherdigits:
        tenpower *= 10 

    result = (lastdigit * tenpower) + otherdigits   #new place of lastdigit appended with the remaining numbers
    return result

n = 10000008
rotated = rotatedigits(n)
print(rotated)
