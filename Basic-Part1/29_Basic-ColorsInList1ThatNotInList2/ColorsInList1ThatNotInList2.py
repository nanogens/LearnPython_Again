'''
29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
'''

def ListDiff(list1, list2):
    #print differences between two lists
    print(list1.difference(list2))
    #print similarities between two lists
    print(list1 & list2)


color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

ListDiff(color_list_1,color_list_2)