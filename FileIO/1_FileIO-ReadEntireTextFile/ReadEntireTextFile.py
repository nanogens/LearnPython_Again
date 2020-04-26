'''
1. Write a Python program to read an entire text file.
'''

'''
Note : 
Tip: __file__ for cross-platform scripts

"That's annoying!", I hear you exclaim, "my pythonanywhere username isn't the same as my local username. and I'm on 
Windows maybe, so paths arent' the same! Relative paths are so convenient! I don't want to run different code on my 
machine and on PA". A very reasonable grumble. But fear not:

import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'myfile.txt')

code like this, based on deriving the current path from Python's magic __file__ variable, will work both locally and 
on the server, both on Windows and on Linux...
'''

'''
Another possibility: case-sensitivity

One other thing that might be going on is that you're using the wRoNG cAsINg. Casing doesn't matter on Windows but 
it does on Linux (and therefore, it matters on PythonAnywhere). So, be consistent with Uppercase and lowercase!
'''

import os

def file_read(fname):
    #This gets the absolute file path for the current directory
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    #This is the file name
    fx = os.path.join(THIS_FOLDER, fname)

    #Open the file - now that we have the absolute path to the file (and the file name) stored in fx
    txt = open(fx)
    #Read the entire file
    print(txt.read())

file_read('test.txt')
