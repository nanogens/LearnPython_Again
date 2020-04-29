'''
5. Write a Python program to get a single string from two given strings, separated by a space and swap the
first two characters of each string. Go to the editor

Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
'''

def StrSwap(str1, str2):
    strx1 = str2[0] + str2[1] + str1[2]
    strx2 = str1[0] + str1[1] + str2[2]
    return(strx1 + " " + strx2)

print(StrSwap("abc","xyz"))
