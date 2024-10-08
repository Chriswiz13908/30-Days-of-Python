#day-3.py

#Arithmetic Operations in Python
#integers

print('Addition:', 1 + 2)
print('Subtraction:', 2 - 1)
print('Multiplication:', 2 * 3)
print('Division', 4 / 2)        #Division in python gives floating number
print('Division:', 6 / 2)
print('Division:', 7 / 2)
print('Division without the remainder:', 7 // 2)   #gives without the floating number or without the remaining
print('Modulus:', 3 % 2)                            #Gives the remainder
print('Division without the remainder:', 7 // 3)
print('Exponential:', 3 ** 2)                        #it means 3 * 3

#Floating numbers
print('Floating Number, PI', 3.14)
print('Floating number, gravity', 9.81)

#complex numbers
print('Complex number:', 1 + 1j)
print('Multiplying complex number:', (1 + 1j) * (1 - 1j))

#Declaring the variable at the top of the first

a = 3  #a is a variable and 3 is an integer data type
b = 2 #b is a variable name and 3 is an integer data type

#Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print('a + b =', total)
print('a - b =', diff)
print('a * b =', product)
print('a / b =', division)
print('a % b =', remainder)
print('a // b =', floor_division)
print('a ** b =', exponential)

#Declaring values and organizing them together
num_one = 3
num_two = 4

#Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

#Printing the values with label
print('total:', total)
print('difference:', diff)
print('product:', product)
print('division:', div)
print('remainder:', remainder)

#calculating area of a circle
radius = 10                               #radius of a circle
area_of_a_circle = 3.14 * radius ** 2     #two * sign means exponent or power
print('Area of a circle:', area_of_a_circle)

#Calculating the area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

#Calculating weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)               #True, because 3 is greater than 2
print(3 >= 2)              #True, becasue 3 is greater than or equal to 2
print(3 < 2)               #False, 3 is greater than 2
print(2 < 3)               #True, 2 is less than 3
print(2 <= 3)              #True, 2 is less than or equal to 3
print(3 == 2)              #False, 3 is not equal to 2
print(3 != 2)              #True, 3 is not equal to 2
print(len('mango') == len('avocado'))    #False
print(len('mango') != len('avocado'))     #True
print(len('mango') < len('avocado'))       #False
print(len('milk') != len('meat'))           #False
print(len('milk') == len('meat'))            #True
print(len('tomato') == len('potato'))         #True
print(len('python') > len('dragon'))           #False

#Boolean comparison
print('True == True:', True == True)
print('True == False:', True == False)
print('False == False:', False == False)
print('True and True', True and True)
print('True or False:', True or False)

#Another way comparison
print('1 is 1', 1 is 1)                     #True, the data values are the same
print('1 is not 2', 1 is not 2)             #Truw, 1 is not 2
print('C in Christopher', 'C' in 'Christopher') #True, C is found in the string
print('c in Christopher', 'c' in 'Christopher') #Fales, lowercase c is not in Christopher
print('coding' in 'coding for all')             #True, coding is in coding for all
print('a in an:', 'a' in 'an')                  #True
print('4 is 2 **2:', 4 is 2 ** 2)               #True

print(3 > 2 and 4 > 3)   #True
print(3 > 2 and 4 < 3) #False
print(3 < 2 and 4 < 3) #False
print(3 > 2 or 4 > 3) #True
print(3 > 2 or 4 < 3) #True
print(3 < 2 or 4 < 3) #False
print(not 3 > 2)   #False, 3 > 2 is true, then not True gives False
print(not True)     #False, Negation, the not operator turns true to false
print(not False)      #True
print(not not True)  #True
print(not not False)   #False