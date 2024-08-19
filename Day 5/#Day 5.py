#Day 5

empty_list = list()  # this is an empty list
print(len(empty_list))

fruit = ['banana', 'orange', 'mango', 'apple']
vegetables = ['carrot', 'cucumber', 'onion']
dairy = ['milk', 'butter', 'yoghurt', 'icecream']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
countries = ['USA', 'Finland', 'Mexico', 'Spain']

# printing the lists and their lengths

print('Fruits:', fruit)
print('How many fruit?', len(fruit))
print('Veggies:', vegetables)
print('How many veggies are we putting in the bunghole?', len(vegetables))
print('What are we cooking with, Senpai?', dairy)
print('Number of dairy products:', len(dairy))
print('Web technologies:', web_techs)
print('Number of known technologies:', len(web_techs))
print('Number of countries:', len(countries))

# Modifying lists

fruit = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruit[0] #we are accessing the first item on the fuit list using its index
print(first_fruit)
second_fruit = fruit[1]
print(second_fruit)
last_fruit = fruit[3]
print(last_fruit)
last_index = len(fruit) - 1
last_fruit = fruit[last_index]

# Accessing items
last_fruit = fruit[-1]
second_lastfruit = fruit[-2]
print(last_fruit)
print(second_lastfruit)

# Slicing items
all_fruit = fruit[0:4] # returns all the fruit list
print(all_fruit)
#below also gives the same result as the above line
all_fruit = fruit[0:] # if we dont set where to stop it takes all the rest
print(all_fruit)
orange_and_mango = fruit[1:3] # does not include the end index
print(orange_and_mango)
orange_mango_lemon = fruit[-3:]
print(orange_mango_lemon)

all_fruit = fruit[-4:] #returns all fruit
print(all_fruit)
orange_and_mango = fruit[-3:-1]
print(orange_and_mango)
orange_mango_lemon = fruit[-3:]
print(orange_mango_lemon)

fruit[0] = 'Avacado' # replaces the first index of list
print(fruit)
fruit[1] = 'Apple'
print(fruit)
last_index = len(fruit) - 1
fruit[last_index] = 'lime'
print(fruit)

# checking items
fruit =['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruit
print(does_exist)
does_exist = 'lime' in fruit
print(does_exist)

# Append - to add to end of list
fruit = ['banana', 'orange', 'mango', 'lemon']
fruit.append('apple')
print(fruit)
fruit.append('lime')
print(fruit)

# insert
fruit = ['banana', 'orange', 'mango', 'lemon']
fruit.insert(2, 'apple') # insert apple between orange and mango making mango the 3 index
print(fruit)
fruit.insert(3, 'lime')
print(fruit)

# remove
fruit = ['banana', 'orange', 'mango', 'lemon']
fruit.remove('banana')
print(fruit)

# pop - deletes by index and returns the value
fruit = ['banana', 'orange', 'mango', 'lemon']
fruit.pop() # when no index is listed, removes last index
print(fruit)
fruit.pop(0)
print(fruit)

# del - deletes by index
fruit = ['banana', 'mango', 'orange', 'lemon']
del fruit[0]
print(fruit)
del fruit[1]
print(fruit)
#del fruit
#print(fruit)

# clear - clears entire list but leaves brackets
fruit = ['banana', 'orange', 'mango', 'lemon']
fruit.clear()
print(fruit)

# copying a list
fruit = ['banana', 'orange', 'mango', 'lemon']
fruit_copy = fruit.copy()
print(fruit_copy)

# join
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruit = ['banana', 'orange', 'mango', 'lemon']
veggies = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruit_and_veggies = fruit + veggies
print(fruit_and_veggies)

# join with extend
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruit = ['banana', 'orange', 'mango', 'lemon']
veggies = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruit.extend(veggies)
print('Fruits and veggies:', fruit)

# count
ages = [22, 13, 19, 99, 67]
print(ages.count(22))

# index
print(ages.index(13))

# Reverse
ages.reverse()
print(ages)

# sort
fruit.sort()
print(fruit)