'''
Lattice paths
Problem 15 

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?

'''

grid = []

length = 21
width = 21

for i in range(0, length):
    temp = []
    for j in range(0, width):
        if i == 0:
            temp.append(1)
        elif j == 0:
            temp.append(1)
        else:
            temp.append(0)
    grid.append(temp)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if i > 0 and j > 0:
            grid[i][j] = grid[i-1][j] + grid[i][j-1]

print grid[len(grid)-1][len(grid[len(grid)-1])-1]