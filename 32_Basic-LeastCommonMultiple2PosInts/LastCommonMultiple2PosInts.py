'''
32. Write a Python program to get the least common multiple (LCM) of two positive integers.
'''

def LCM(num1,num2):
    if(num1 > num2):
        numx = num2
    else:
        numx = num1

    for x in range(numx - 1):
        if(num1 % int(x + 1) == 0):
            save1 = x
        if(num2 % int(x + 1) == 0):
            save2 = x
        if(save1 == save2):
            save12 = x
            break;

LCM(6,9)