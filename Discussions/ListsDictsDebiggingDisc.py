# PROBLEM 1
""" You're writing your own implementation of the map function which
takes in a one-argument function and applies it to every element in a list
and returns a new list. However, you are running into some bugs.
The is what you expect to happen:

>>> def double(x):
return x*2
>>> lst = [1, 2, 3]
>>> my_map(double, lst)
[2, 4, 6]

This is the code you've written so far:
    1 def my_map(func, seq):
    2 res = []
    3 for i in seq:
    4 curr = func(seq[i])
    5 res.append(curr)
    6 return res

This is the error you get:
    >>> my_map(double, lst)
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "/Users/yourname/pydecal/my_map.py", line 4, in my_map
            curr = func(seq[i])
    IndexError: list index out of range"""

# PART 1
""" What line is your error on? """
print("The error is on line: ", "4")
# PART 2
""" Rewrite that line to correct the error
Please keep the code in quotes!"""
print("The line should be: ", "curr = func(i)")


percentages = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]
max_score = 300

scores = [[int(percent * max_score) for percent in percentages]]

print('Scores corresponding to the given percentages, on a scale out of 300:')
print(scores)

patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

for patient in patients:
    weight, height = patient
    bmi = calculate_bmi(weight,height)
    print(f'patients BMI is: {bmi}')