binary = input('Enter a string of bits: ')
decimal = 0
exponent = len(binary) - 1

for digits in binary:
    decimal = decimal + int(digits) * 2 ** exponent
    exponent -= 1
print('The integer value of', binary, 'is', decimal)