plain_text = input('Enter lowercase text: ')
distance = int(input('Enter distance: '))
code = ''

for ch in plain_text:
    ord_Value = ord(ch)
    cipher_Value = ord_Value + distance
    if cipher_Value > ord('z'):
        cipher_Value = ord('a') + distance -(ord('z') - ord_Value + 1)   
    code += chr(cipher_Value)
print(code)

empty = ''
for ch in code: 
    ord_Value = ord(ch)
    cypher_Value = ord_Value - distance
    if cypher_Value < ord('a'):
        cypher_Value = ord('z') - (distance - (ord('a') - ord_Value + 1))
    empty += chr(cypher_Value)
print(empty)