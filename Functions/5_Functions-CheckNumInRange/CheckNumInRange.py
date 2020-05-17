'''
Write a Python function to check whether a number is in a given range.
'''

def CheckNumbRange(num,lowrange,highrange):
    if(num > lowrange) and (num < highrange):
        return "True"
    else:
        return "False"

print(CheckNumbRange(5,7,10))