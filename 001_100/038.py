'''
Pandigital multiples
Problem 38 

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

from tqdm import tqdm
result = set()

for i in tqdm(range(1, 10000)):
    start = 1
    pandigital = []
    myFlag = True
    while myFlag:
        tempResult = start * i
        strResult = str(tempResult)
        for j in strResult:
            if j in pandigital or j == '0':
                myFlag = False
                break
            pandigital.append(j)
        if len(pandigital) == 9:
            onceResult = ''
            for x in range(0, 9):
                onceResult += pandigital[x]
            print onceResult, i
            result.add(int(onceResult))
            break
        elif len(pandigital) > 9:
            break
        start += 1
    
print max(result)