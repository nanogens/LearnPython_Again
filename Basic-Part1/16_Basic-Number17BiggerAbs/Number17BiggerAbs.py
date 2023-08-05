'''
16. Write a Python program to get the difference between a given number and 17, if the number is
greater than 17 return double the absolute difference.
'''

number = input("\nEnter a number: ")
diff = int(number) - 17
if diff > 0:
    print("\nAbs difference multiplied by 2 if number is positive: " + str(abs(diff)*2))
else:
    print("\nNumber is negative: " + str(diff))