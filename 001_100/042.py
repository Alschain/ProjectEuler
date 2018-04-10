'''
Coded triangle numbers
Problem 42 

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

WORDS = []
alpDict = {}
triangle = []

with open('p042_words.txt', 'r') as f:
    contents = f.read()
    WORDS = contents.split(',')

for i in range(0,26):
    alpDict[chr(ord('A') + i)] = i + 1

def cal_word(word):
    result = 0
    word = word[1:-1]
    for x in word:
        result += alpDict[x]
    return result


for i in range(1, 21):
    triangle.append(i * (i + 1) / 2)

result = 0

for word in WORDS:
    if cal_word(word) in triangle:
        result += 1

print result