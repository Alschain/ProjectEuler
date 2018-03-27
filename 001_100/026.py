'''
Reciprocal cycles
Problem 26 

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

'''
With Fermat's little theorem

for all positive interger a, a = 1 mod p

then 10^(p-1) = 1 mod p

let 10^(p-1) - 1 = kp

then 1 / p equals k / {9...9} (p-1)

so the recurring cycle length is p-1 or the divisor of p-1
'''

def get_recurring_length(n):
    count = 1
    while True:
        if pow(10, count) % n == 1:
            return count
        count += 1

NUMS = [i for i in range(0, 1000)]

greatest = 1
result = 1

from tqdm import tqdm
for i in tqdm(range(2, len(NUMS))):
    if NUMS[i] % 2 == 0 or NUMS[i] % 5 == 0:
        continue
    length = get_recurring_length(NUMS[i])
    if length > greatest:
        greatest = length
        result = i

print result, greatest