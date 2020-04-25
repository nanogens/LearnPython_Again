'''
27. Write a Python program to concatenate all elements in a list into a string and return it.
'''

def Concat(l):
    str = ""
    chra = "";
    y = 0
    for a in l:
        str = str + l[y];
        y = y + 1
    print("\n" + str)

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

lis = ["Hello ", "how ", "are ", "you "]
Concat(lis)

print(concatenate_list_data(lis))
