'''
34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
'''

def SumOf2IntsRet20If15to20(num1,num2):
    numx = num1 + num2
    if(numx >= 15) and (numx <= 20):
        return 20
    else:
        return numx

print("\n")
print(SumOf2IntsRet20If15to20(5, 100))
print(SumOf2IntsRet20If15to20(5, 12))
print(SumOf2IntsRet20If15to20(15, 10))
print(SumOf2IntsRet20If15to20(0, 17))