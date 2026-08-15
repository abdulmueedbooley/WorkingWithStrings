
#* String Length
print(len("hi there"))

#* Subscript operator - [] is your primary tool for accessing individual characters within a string.
#* Think of it as a way to pin point and extract the exact character you need from any position 
name = 'Abdul mueed'
print(name[0])
print(name[3])

#* The 2 alternatives to pin point and extract the last character
#* OPTION ONE
print(name[len(name) - 1])
#* OPTION TWO
print(name[-1])


#* USING SUBSCRIPT OPERATOR IN LOOPS
data = 'Abdul Booley' 
for index in range(len(data)):
    print(index, data[index])

#* STRING SLICING
# string[start : end] - extracts characters from start up to (but not inlcuding) end
name = 'Abdul'
print(name[0:]) #*? How to extract the entire string?
print(name[ :len(name)]) #*? What is an alternative to extract the entire string
print(name[0:1]) #*? How to extract the FIRST LETTER of the string? 
print(name[-3:]) #*? How to extract the LAST THREE letters of the string

#* TESTING FOR A SUBSTRING WITH THE "in" OPERATOR
#*? what is a SUBSTRING?
# A SUBSTRING is a smaller piece of text made up of characters that sit next to eachtoher inside a larger string
# FOR EXAMPLE the word "cat". "ca", "cat","at" are valid because the letters are in the corect order. 
# HOWEVER "ct" is not valid because the letters are in the incorrect order

filelist = ["myfile.txt", "myprogram.exe", "yourfile.txt"]
for filename in filelist:
    if ".txt" in filename:
        print(filename)

