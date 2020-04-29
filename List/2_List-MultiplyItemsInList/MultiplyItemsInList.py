'''
2. Write a Python program to multiply all the items in a list.
'''

list = ([1,2,3,4,5])

def mult_list(lst):
    #we start with 1 so that the first number in the list is multiplied by 1 instead of 0
    tot = 1
    #note x represents the actual value in the list, not an index position
    #so we can multiply by x directly instead of lst[x]
    for x in lst:
        tot *= x
    return tot

print("\nResult of numbers in list multiplied: " + str(mult_list(list)))