name = 'Coby is a good boy'

#length of string including space and punctuations
print(len(name))
# print index of first occurance of letter 'g'
print(name.index('g'))
# prints count of letter 'o' in given string
print(name.count('o'))
# print part of string based on index, string is considered as list of chatacter, so we can apply slicing here
# all list slicing techniques apply here as well
print(name[2:8]) # print from index 2 included to index 7 ( end index is excluded)
print(name.lower())
print(name.upper())
print(name.isupper())
print(name.islower())
print(name.isalnum())
print(name.isalpha())
print(name.isnumeric())
print(name.split())

