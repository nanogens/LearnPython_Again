'''
4. Write a Python program to read last n lines of a file.
'''

import sys
import os
def file_read_from_tail(fname,lines):
        bufsize = 8192
        fsize = os.stat(fname).st_size
        iter = 0
        with open(fname) as f:
                if bufsize > fsize:
                        bufsize = fsize-1
                        data = []
                        while True:
                                iter +=1
                                # this turns out to be the value 1
                                f.seek(fsize-bufsize*iter)
                                #data will contain all lines of the file
                                data.extend(f.readlines())
                                #len(data) contains the number of lines
                                if len(data) >= lines or f.tell() == 0:
                                        print(''.join(data[-lines:]))
                                        break

file_read_from_tail('abc.txt',3)
