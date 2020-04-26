'''
7. Write a Python program to accept a filename from the user and print the extension of that.
'''

filename = input("\nEnter a file name with its extension (e.g. java.txt): ")
f_extns = filename.split(".")
print("The extension of the file is: " + repr(f_extns[-1]))

#Alternate solution
#MT : Not really sure I understand sep and maxsplit usage but including it here anyways.
'''
Sample filename: abc.java

Python str.rsplit(sep=None, maxsplit=-1) function:

The function returns a list of the words of a given string using a separator as the delimiter string.

    If maxsplit is given, the list will have at most maxsplit+1 elements.
    If maxsplit is not specified or -1, then there is no limit on the number of splits.
    If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings.
    The sep argument may consist of multiple characters.
    Splitting an empty string with a specified separator returns [''].
'''
f_extns2 = filename.rsplit(sep=".",maxsplit=1)  # can be split as well instead of rsplit
print("\nThe extension of the file is: " + repr(f_extns2[-1]))