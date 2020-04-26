'''
2. Write a Python program to read first n lines of a file.
'''

import os

def file_read_from_head(fname,nlines):
    #This gets the absolute file path for the current directory
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    #This is the file name
    fx = os.path.join(THIS_FOLDER, fname)

    #Open the file - now that we have the absolute path to the file (and the file name) stored in fx
    from itertools import islice
    with open(fx) as f:
        for line in islice(f, nlines):
            print(line)

file_read_from_head('test.txt', 2)
