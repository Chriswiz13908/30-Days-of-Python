#variables in Python

first_name = 'Christopher'
last_name = 'Wolverton'
country = 'The United States of America'
city = 'Beckley'
age = 28
is_married = False
skills = ['Python', 'Cooking', 'Gaming']
person_info = {
    'firstname': 'Christopher',
    'lastname' : 'Wolverton',
    'country' : 'The United States of America',
    'city' : 'Beckley'
}

#Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name:', last_name)
print('Last name length:', len(last_name))
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Married:', is_married)
print('Skills:', skills)
print('Personal information:', person_info)

#Declaring multiple variables in one line

first_name, last_name, country, age, is_married, = 'Christopher', 'Wolverton', 'The United States of America', 28, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name:', last_name)
print('Country', country)
print('Age:', age)
print('Married:', is_married)