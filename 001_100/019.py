'''
Counting Sundays
Problem 19 

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

months = [31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


sum = 0

day = 1
for i in range(1901, 2001):
    if is_leap(i):
        months[1] = 29
    else:
        months[1] = 28
    
    for j in range(0, 12):
        day = (day + months[j]) % 7
        if day == 6:
            sum += 1

print sum