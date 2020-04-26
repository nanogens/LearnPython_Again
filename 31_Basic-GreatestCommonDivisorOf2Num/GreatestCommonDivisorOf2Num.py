'''
31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
'''

def GCD(num1,num2):
    if(num1 > num2):
        numx = num2
    else:
        numx = num1

    for x in range(numx):
        if(num1 % int(x) == 0) and (num2 % int(x) == 0) and (x != 0):
            save12 = x
    print(save12 + 1)

GCD(5,10)