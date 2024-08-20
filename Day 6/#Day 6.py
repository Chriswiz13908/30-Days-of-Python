#creating tuples

tuple()

brother = ('Austin', 'Bob')
print(brother)

sisters = ('Katie', 'Anna')
print(sisters)

#converting tuples to lists to modify them
brother = list(brother)
print(brother)

sisters = list(sisters)
print(sisters)

#joining the tuples/lists
siblings = sisters + brother
print(siblings)

#checking length
print("How many siblings?", len(siblings))

siblings = list(siblings) 
print(siblings)

#Modifying siblings and parents to create family members
parents = ('Mom', 'Dad')
print(parents)

parents = list(parents)
print(parents)

family_members = parents + siblings
print(family_members)

#unpacking
str = family_members[0:2]
print(str)

#Creating three new tuples, joining and assigning to food stuff tple
fruits = ('Mango', "Apple")
print(fruits)

vegetables = ('Carrot', 'Squash')
print(vegetables)

animal_products = ('Meat', 'Dairy')
print(animal_products)

fruits = list(fruits)
print(fruits)

vegetables = list(vegetables)
print(vegetables)

animal_products = list(animal_products)
print(animal_products)

food_stuff_tp = animal_products + vegetables + fruits
print(food_stuff_tp)

#chagnging to list and slicing
food_stuff_tp = list(food_stuff_tp)
food_stuff_lt = food_stuff_tp
print(food_stuff_lt)

carrot = food_stuff_lt[2]
print(carrot)

first_and_last = food_stuff_lt[0] + ',' + ' ' + food_stuff_lt[5]
print(first_and_last)

del(food_stuff_tp)
print('Meat' in food_stuff_lt)

print('Meat' in food_stuff_lt)