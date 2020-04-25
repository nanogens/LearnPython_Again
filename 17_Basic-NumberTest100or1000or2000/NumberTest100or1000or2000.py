'''
17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
'''

number = int(input("Enter a number: "))
if (1900 < number < 2100) or (900 < number < 1100):
    print("\nNumber is within 100 of 1000 or 2000")
else:
    print("\nNumber is not within 100 of 1000 or 2000")