'''
19. Write a Python program to get a new string from a given string where "Is" has been added to the front.
If the given string already begins with "Is" then return the string unchanged.
e.g. My name is Manish = Is My name Manish
     Is my name Manish = Is My name Manish
'''

str1 = input("Enter a string: ")
str2 = str1.split(sep="Is",maxsplit=-1)
#If the Is has been split off, it won't be there so I'm comparing it to ''
if(str2[0] == ''):
    print(str1)
else:
    print("Is " + str1)

