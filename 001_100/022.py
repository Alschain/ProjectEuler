'''
Names scores
Problem 22 

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''


worthDict = {}


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(0, len(ALPHABET)):
    worthDict[ALPHABET[i]] = i + 1

def get_worth(name):
    result = 0
    for i in range(len(name)):
        result += worthDict[name[i]]
    
    return result


NAMES = []
with open('p022_names.txt', 'r') as f:
    content = f.read()
    NAMES = content.split(',')

result = 0

NAMES = sorted(NAMES)

for i in range(len(NAMES)):
    NAMES[i] = NAMES[i][1:-1]
    result += (i + 1) * get_worth(NAMES[i])

print result