#Write a function that takes in an integer and returns the sum of the digits
#(the digital root).
#[Ex]: digital root(12345) will return 15

def digitalroot(n):
    while n >= 1:
        digisum = 0
        while n > 0:
            digit = n % 10
            digisum += digit
            n //= 10
        n = digisum 
    return n 

number = 12345
print('Digital Root:', digitalroot(number))