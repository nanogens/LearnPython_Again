'''
Write a Python function to sum all the numbers in a list.
'''

def Sum(lst):
    sumit = 0
    for i in lst:
        sumit += i
    return sumit

print(Sum([2,2,2]))