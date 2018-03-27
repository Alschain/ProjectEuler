'''
Coin sums
Problem 31 

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

COINS = [1, 2, 5, 10, 20, 50, 100, 200]

dp = [[0 for i in range(len(COINS))] for j in range(201)] # dp[i][j] money i with coins no more than COINS[j]


dp[0][0] = 1
for i in range(len(dp)):
    for n, coin in enumerate(COINS):
        if coin > i:
            continue
        for k in range(n+1):
            dp[i][n] += dp[i - coin][k]

print sum(dp[200])
        