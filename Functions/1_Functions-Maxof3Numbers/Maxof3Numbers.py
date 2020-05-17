'''
Write a Python function to find the Max of three numbers.
'''

def MaxOf3(one,two,three):
    if(one >= two) and (one >= three):
        #one is biggest
        return one
    elif(two >= one) and (two >= three):
        #two is biggest
        return two
    elif(three >= one) and (three >= two):
        #three is biggest
        return three

def MaxOf3Alt(nums):
    i_prev = 0
    for i in nums:
        if(i > i_prev):
            highest_num = i
        i_prev = i
    return highest_num


print(MaxOf3(4,22,3))

print(MaxOf3Alt([4,22,3]))
