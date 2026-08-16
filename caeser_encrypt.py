
#* Booley
plain_text = input('Enter lowercase text: ')
#* distance = 3
distance = int(input('Enter distance: '))
#* Empty string to store encrypted letters
code = ''
#* iterating through each character and converting them into there ASCII value 
for ch in plain_text:
    # 'y' = 121
    ord_Value = ord(ch)
    # 124 = 121 + 3
    cipher_Value = ord_Value + distance
    #* if 124 > 122 (in this case the condition is true)
    if cipher_Value > ord('z'):
        #* In this method we need to wrap - around the lowercase alphabet
        #* Within the parenthesis we find the difference between the 2 letters (ord('z') - ord_Value + 1)
        #* Once we have found the difference we ' + 1' used as an extra step to wrap back to lowercase 'a'
        #* The extra steps are then added to ord('a') = 97 + 3 - 2 = 98
        #* chr(98) = 'b' ('b' is the encrypted value)
        cipher_Value = ord('a') + distance -(ord('z') - ord_Value + 1)
    # After each iteration the NEW encrypted letter gets stored into the empty string
    # REMEMBER the cipher_value is still a number so dont forget to integrate the chr() function 
    # This converts an integer to a string    
    code += chr(cipher_Value)
print(code)