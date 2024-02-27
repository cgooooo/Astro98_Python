#Calculate BMI

people = [[182,5.6],[130,5.5],[60,3.6]]
def bmi_calc (weight,height):
    return weight / (height**2)

for person in people:
    weight, height  = person
    bmi = bmi_calc(weight, height)
    print (f'persons BMI is: {bmi}')
    