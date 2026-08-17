decimal = int(input('Enter an integer: '))

if decimal == 0:
    print('0')
    print('The binary representaton is 0')
else:
    print('Quotient', 'Remainder', 'Binary')
    string_bits = ''
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        string_bits = str(remainder) + string_bits
        print(decimal, remainder, string_bits)

print('The binary representation is', string_bits)
