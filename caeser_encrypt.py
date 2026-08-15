plaintext = input('Enter a lower case word: ')
distance = int(input('Enter distance between letters:'))
code = ""
for ch in plaintext:
    ordValue = ord(ch)
    ciphervalue = ordValue + distance
    #* Check if the shifted letter goes past 'z' (out of the lowercase alphabet)
    if ciphervalue > ord('z'):
        #* If it does wrap back around 'a' by calculating
        #* the remaining shift distance and applying it from 'a'
        ciphervalue = ord('a') + distance - (ord('z') - ordvalue + 1)
    code += chr(ciphervalue)
print(code)


