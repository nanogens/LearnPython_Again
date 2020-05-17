'''
Write a Python class to find a pair of elements (indices of the two numbers) from a given
array whose sum equals a specific target number.
'''

#MT Note : In this example, the sum of the number will always be a number and the next number beside it.

#Actual Solution
class py_solution:
   def twoSum(self, nums, target):
        lookup = {}
        #lookup[0] = 10
        #lookup[1] = 20
        #return (lookup[0],1)
        for i, num in enumerate(nums):
            if target - num in lookup:
                print(target, num)
                print(lookup[target - num], i)
                return (lookup[target - num], i) #position of previous number committed to lookup, present position
            lookup[num] = i

print("index1=%d, index2=%d" % py_solution().twoSum((10,20,10,40,50,60,70),90))
