'''
14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''

from datetime import date
f_date = date(1991,12,30)
e_date = date(2020,4,23)
delta = e_date - f_date;
print(delta)