'''
3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return instead of the empty string.

Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
'''

def string_both_ends(str):
  if len(str) < 2:
    return ''
  return str[0:2] + str[-2:]

def string_test(str):
    return str[2:] #will spell our resource.  OR you can write it from the position -8 (r) to the end [-8:]

print(string_both_ends('w3resource')) #w3ce
print(string_both_ends('w3')) #w3w3
print(string_both_ends('w')) #returns

print(string_test('w3resource')) #spells out resource
