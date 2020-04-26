'''
 Write a Python program to get a string which is n (non-negative integer) copies of a given string.
'''

def largerstring(str, n):
    result = ""
    for i in range(n):
        result = result + str;
    return result

print(largerstring(".abc",3))
print(largerstring(".xyz",2))