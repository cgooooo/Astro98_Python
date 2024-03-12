#Write a function that takes a year as input and returns True if it’s a leap
#year, and False otherwise. A leap year is divisible by 4 but not divisible by
#100 unless it is also divisible by 400.

def leapcheck(i):
    if i % 4 == 0:
        if i % 100 == 0:
            if i % 400 == 0: 
                return True         #True if divisible by 400
            else: 
                return False        #if not divisible by 400 false 
        else: 
            return True             #if divisible by 400 and 100 true 
    else: 
        return False                #if not divisible by 4 false
               
        
i = 2004
print(leapcheck(i), i)