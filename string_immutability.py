# If your string contains double quotes or single quotes
# we have 2 options
# Option 1: We use the opposite quotes for example
my_string = "It's a beautiful day"
print(my_string)

# Option 2: We make use of an escape sequence the backslash "\"
my_string = 'It\'s a beautiful day'
print(my_string)

# we make use of the IN operator to check for specific characters/ character within a string
# The IN operator returns a boolean value
my_string = 'hello world'
print('hello' in my_string) # returns true
print('i' in my_string) # returns false

# Mutable means that it can be changed after it is created
# Immutable means that it cannot be changed after it has been created 
greeting = 'hello'
greeting = 'hi'
print(greeting)

# However direct modification is not allowed 
greeting = 'hi'
greeting[0] = 'hi'
# NOTE that integers, floats and booleans are also immutable


