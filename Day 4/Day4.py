
#Single line coment
letter = 'P'            # A string could be a single character or a bunch of texts
print(letter)           # P
print(len(letter))      # 1
greeting = 'Welcome, Buttface!'      # String could be a single or double qoute, "Welcome, Buttface!"
print(greeting)                      # Welcome, Buttface!
print(len(greeting))                 # 18
sentence = "I don't need you, Buttface!"
print(sentence)

# Multiline String
multiline_string = '''I eat ass and enjoy rubbing rusty spoons on my fingers. 
I can't find my spoons though. Do you have my spoons?'''
print(multiline_string)
# Same but using triple double quotes
multiline_string = """I eat ass and enjoy rubbing rusty spoons on my fingers.
I can't find my spoons though. Do you have my spoons?"""

# String concatenation
first_name = 'Christopher'
last_name = 'Wolverton'
space = ' '
full_name = first_name + space + last_name
print(full_name)
# Check length of a string using len() builtin function
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

# Upacking characters
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence charaters into variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter)
second_last = language[-2]
print(second_last)

# Slicing
first_three = language[0:3] # Starts at zero index and up to 3 but not including 3
last_three = language[3:6]
print(last_three)
# Another way
last_three = language[-3:]
print(last_three)
last_three = language[3:]
print(last_three)

# Skipping character while splitting Python strings
pto = language[0:6:2]
print(pto)

# Escape sequence
print('I hope you are enjoying this challenge. \nare you?') # line break \n
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash symbol(\\)') # To write the back slash
print('In every programming language it starts with \"Hello, World!\"')

# String Methods
# .capitalize(): Converts the first characteer of the string to a Capital Letter

challenge = 'thirty days of python'
print(challenge.capitalize())

# Count(): returns occurences of substring in string, count(substring, start=.., end=..)
print(challenge.count('y'))
print(challenge.count('y, 7, 14'))
print(challenge.count('th'))

# endswith(): Checks if a string ends with a specified ending
print(challenge.endswith('on'))
print(challenge.endswith('tion'))

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument.
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

# find(): Returns the index of first occurence substring
challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))

# format(): formats string into nicer output
first_name = 'Christopher'
last_name = 'Wolverton'
job = 'Chef'
country = 'USA'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence)

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with {} is {}'.format(str(radius), str(area))  #radius and area are integers, so the str() turns them into strings
print(result)

# index(): Returns the index of a substring
challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))

# isalnum(): checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())

challenge = '30DaysPython'
print(challenge.isalnum())

challenge = 'thirty days of python'
print(challenge.isalnum())

challenge = 'thirt days of python 2024'   # the spaces causes the string to return false because spaces are neither part of the alphabet nor are they numbers, spaces count as characters
print(challenge.isalnum())

# isalpha(): Checks if all characters are alphabets

challenge = 'thirty days of python'
print(challenge.isalpha())  # false cause of spaces

challenge = 'thirtydaysofpython'
print(challenge.isalpha())  # true because of no spaces

num = '123'
print(num.isalpha())

# isdecimal(): Checks Decimal Characters
challenge = 'thirty days of python'
print(challenge.isdecimal())

challenge = '1259'
print(challenge.isdecimal())   # Returns true only if the str consists of all decimal characters with no alphabets, no whitespaces, no special characters, not floating point numbers, and no separaters.

#isdigit(): Checks Digit Characters

challenge = 'Thirty'
print(challenge.isdigit())
challenge = '30'
print(challenge.isdigit())

# isidentifier(): Checks for valid identifier, means it checks if a string is a valid variable name

challenge = '30DaysOfPython'
print(challenge.isidentifier()) #False because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())


# islower(): Checks if all alphabets in a string are lowercase

challenge = 'thirty days of python'
print(challenge.islower())
challenge = 'Thirty days of python'
print(challenge.islower())

# isupper(): checks if all are uppercase

challenge = 'thirty days of python'
print(challenge.isupper())
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())

# isnumeric(): Checks numeric characters

num = '10'
print(num.isnumeric())

# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'Javascript', 'React']
result = '#, '.join(web_tech)
print(result)

# strip(): Removes both leading and trailing characters

challenge = ' thirty days of python '
print(challenge.strip())

# replace(): Replaces substring inside

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))

# split(): Splits string from left

challenge = 'thirty days of python'
print(challenge.split())

# title(): Returns a title cased string

challenge = 'thirty days of python'
print(challenge.title())

# swapcase(): Swaps uppercase with lower and viceversa
challenge = 'thirty days of python'
print(challenge.swapcase())

# startswith(): Chcks if string starts with specified string

challenge = 'thirty days of python'
print(challenge.startswith('thirty'))
print(challenge.startswith('30'))