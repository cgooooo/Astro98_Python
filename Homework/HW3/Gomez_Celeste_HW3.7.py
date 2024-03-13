#Write a function which takes in a string and outputs the number of vowels.
#Consider only a,e,i,o,u to be vowels and do not forget about capital letters.
#Ex: vowel count(”UC Berkeley”) will return 41

def vowelcount(word):
    vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U' }
    count = 0

    for i in word:
        if i in vowels:
            count += 1
    return count

myWord = "cacapoopoo"
print('Vowel Count:', vowelcount(myWord))