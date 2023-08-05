'''
18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return
three times of their sum.
'''

numbers = input("Enter three numbers separated by commas: ")
num = numbers.split(sep=",",maxsplit=-1)
numb = int(num[0]) + int(num[1]) + int(num[2])
#numb = int(num[1])
#print(str(numb))
if(int(num[0]) and int(num[1]) and int(num[2]) == 1):
    numb = numb * 3
    #print(str(num[0]) + " " + str(num[1]) + " " + str(num[2]))
#elif:
    #print(str(num[0]) + " " + str(num[1]) + " " + str(num[2]))

print(str(numb))