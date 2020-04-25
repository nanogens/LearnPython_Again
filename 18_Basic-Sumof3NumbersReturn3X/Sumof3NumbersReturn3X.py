'''
18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return
three times of their sum.
'''

numbers = input("Enter three numbers separated by commas: ")
num = numbers.split(sep=",",maxsplit=-1)
if(num[0] and num[1] and num[2]):
    numbers = num[0] + num[1] + num[2]
    print(str(num[0]) + " " + str(num[1]) + " " + str(num[2]))


print(str(num[0]) + " " + str(second) + " " + str(third[0]))