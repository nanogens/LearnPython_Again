'''
1. Write a Python program to calculate the length of a string.
'''

str = "What the heck"

def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count

print(len(str))

print(string_length(str))