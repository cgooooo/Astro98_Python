#Lists 
#a collection of items in a particular order, can store numbers, other lists, strings 
#list uses SQUARE BRACKETS 

#list = [1,2,3]
#months = []     #empty list for when you dont know the values yet

#python starts counting at 0 
#fruits = ["apple", "banana", "orange", "grape"]
#fruits.append("pear")

#Dictionaries
#dict = {key1 : value, key2 : value2}
    #uses CURLY BRACKETS 

planets = []
planets.append("Mercury")
planets.append("Earth")
planets.append("Mars")
print(planets)

planets.insert(1, "Venus")
print(planets)

print(planets[2])

planets[3]="Ares"
print(planets)

planets.append("Jupiter")
print(planets)

planets.remove("Jupiter")
print(planets)

print(len(planets))


#slicing and striding 
#concatenating lists 
    #array1 = [1,2,3]
    #array2 =[4,5,6]

nums = [1,2,3,4,5,6,7,8,9]
sliced = nums[1:9]
print(len(sliced))
print(sliced)
reversed = nums[8::-2]
print(reversed)

#
list1 = ["a","b","c"]
list2 = [17,18,19]
add = list1 + list2
print(add)

#attaching list3 to list1 to create a new list
list3 = [True,False,False]
list1.extend(list3)
print(list1)

#Selecting items in a list that have a specific quality
desserts = ["cake", "icecream", "cookie", "brownie"]
cwords = [dessert.upper() for dessert in desserts if dessert.startswith('c')]
print(cwords)

