star = '*'
print(star)
for count in range(0, 3):
    star *= 2
    print(star)

# String interpolation
name = 'abdul'
age = 19
print(f'My name is {name} and iam {age} years old')

# String slicing - allows you to extract a portion of a string can be identified by its index 
# starting from zero and accessed using the bracket notation
my_string = 'Hello world!'
print(my_string[1:5])
# This extracts everything from index 0 up to (but not including), the character at index 7.
# this is what happens if you omit the stop index
print(my_string[8:])
# default 0 indices
print(my_string[:7])
# extracts the entire string 
print(my_string[:])
# there is also a step parameter, the value used to increment betweem which index in the slice
# string[start:stop:step]
print(my_string[0:11:2])

# another helpful trick is to reverse the string by leaving the start and stop blank 
print(my_string[::-1])

# uppercase 
print(my_string.upper())

# lowercase 
print(my_string.lower())

# returns a string where the specified leading and trailing characters are removed
my_string = '   hello world '
print(my_string.strip())

# replace(old, new)
print(my_string.replace('hello', 'hi').strip())

# split() splits a string and returns a list
split = my_string.split()
print(split)

# join() joins the strings in a collection into a single string with a seperator
my_list = ['hello', 'world']
joined = ' '.join(my_list)

# startswith() returns a boolean indicating if the string starts with a prefix 
print(my_string.startswith('hello'))
# endswith() returns a boolean indicating if the string ends with a suffix

# find() returns the index of the first occurence of substring or -1 if it doesnt find one
print(my_string.find('world'))

# count() returns how many times  a substring appears in a string 
print(my_string.count('o'))

# capatalized() returns the first character as an uppercase and the rest as lowercase 
print(my_string.capitalize())

# isupper() and islower() returns a boolean value
print(my_string.isupper())
print(my_string.islower())

# title() returns a new string with the first letter of each word capatalized 
print(my_string.title())
