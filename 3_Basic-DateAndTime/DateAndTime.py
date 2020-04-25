'''
3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
'''

# Actual Solution
import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%M-%D  %H-%M-%S"))