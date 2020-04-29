'''
3. Write a Python program to append text to a file and display the text.
'''

def file_read(fname):
    from itertools import islice  # import something
    with open(fname,"a") as myfile: # open fname with a handle to the file called myfile
        myfile.write("\n\nPython Exercises\n")
        myfile.write("Java Exercises")
    txt = open(fname) # open the file again
    print(txt.read()) # read from the file

file_read('abc.txt')
