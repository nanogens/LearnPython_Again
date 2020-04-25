'''
22. Write a Python program to count the number 4 in a given list.
'''

def count4(num):
    count = 0
    for x in num:
        if(x == 4):
            count = count + 1
    print("\nCount : " + str(count))
    return count

count4([1,4,6,4,2,1,6])