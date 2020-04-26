'''
33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
'''

def SumOfIntZero2(num1,num2,num3):
    if(num1 == num2) or (num2 == num3) or (num1 == num3):
        return 0
    else:
        numsum = num1 + num2 + num3
        return numsum

print("\n")
print(SumOfIntZero2(1,2,3))
print(SumOfIntZero2(2,2,3))
print(SumOfIntZero2(1,3,3))
print(SumOfIntZero2(1,5,3))