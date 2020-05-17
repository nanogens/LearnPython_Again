'''
Write a Python program to reverse a string.
'''

def string_reverse(str1):
    revstr = ""
    index = 0
    strlen = len(str1) - 1
    while strlen >= index:
        revstr += str1[strlen - index]
        index += 1
    return revstr


print(string_reverse("1234abcd"))
