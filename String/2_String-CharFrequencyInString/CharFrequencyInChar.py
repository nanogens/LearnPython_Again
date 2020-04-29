'''
Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        #increment the existing key if it exists, otherwise increament a new key
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(char_frequency('google.com'))
