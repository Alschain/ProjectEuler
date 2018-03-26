'''
Number letter counts
Problem 17 

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def cal_letters(n):
    sum = 0
    if n >= 0 and n < 20:
        sum += len(ONES[n])
    elif n < 100:
        sum += len(TENS[n / 10]) + (len(ONES[n % 10]) if n % 10 != 0 else 0)
    elif n < 1000:
        sum += len(ONES[n / 100]) + 7 + (cal_letters(n % 100)+3 if n % 100 != 0 else 0)
    elif n < 1000000:
        sum += cal_letters(n / 1000) + 8 + (cal_letters(n % 1000) if n % 1000 != 0 else 0)

    return sum

result = 0
for i in range(1,1001):
    result += cal_letters(i)

print result