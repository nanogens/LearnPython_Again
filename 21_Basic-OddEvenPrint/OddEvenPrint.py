'''
Write a Python program to find whether a given number (accept from the user) is even or odd, print out an
appropriate message to the user.
'''

def number(num):
    if(num % 2 == 0):
        print("\nEven number.")
    else:
        print("\nOdd number.")

number(4)
number(5)
number(8)