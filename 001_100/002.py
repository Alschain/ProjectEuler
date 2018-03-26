'''
Even Fibonacci numbers
Problem 2 

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

F1 = 1
F2 = 2

sum = 2

while True:
    F1 = F1 + F2
    F1, F2 = F2, F1
    sum += F2 if F2 % 2 == 0 else 0
    if F2 >= 4000000:
        break

print sum