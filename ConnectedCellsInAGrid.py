from collections import deque

# Test case:
grid = [[1, 0, 1, 0, 1],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1]]

def p(grid):
    for line in grid:
        print(line)
    print()

def connectedCell(grid, start):
    stack = deque()
    count = 0
    
    m = len(grid)
    n = len(grid[0])
    stack.append(start)
    grid[start[0]][start[1]] = 0
    
    while True:
        if len(stack) == 0: # Is the region finished?
            return count

        loc = stack.pop() # pop top location
        i = loc[0]        
        j = loc[1]
        count += 1        # count it
        
#         print(loc)
#         p(grid)
#         print(stack)

        # push valid neighbors, and erase them
        if i > 0 and j > 0: # up left
            if grid[i - 1][j - 1]: 
                stack.append((i - 1, j - 1))
                grid[i - 1][j - 1] = 0
        if j > 0: # left
            if grid[i][j - 1]:
                stack.append((i, j - 1))
                grid[i][j - 1] = 0
        if i < m - 1 and j > 0: # down left
            if grid[i + 1][j - 1]:
                stack.append((i + 1, j - 1))
                grid[i + 1][j - 1] = 0
        if i < m - 1: # down
            if grid[i + 1][j]:
                stack.append((i + 1, j))
                grid[i + 1][j] = 0
        if i < m - 1 and j < n - 1: # down right
            if grid[i + 1][j + 1]:
                stack.append((i + 1, j + 1))
                grid[i + 1][j + 1] = 0
        if j < n - 1: # right
            if grid[i][j + 1]:
                stack.append((i, j + 1))
                grid[i][j + 1] = 0
        if i > 0 and j < n - 1: # up right
            if grid[i - 1][j + 1]:
                stack.append((i - 1, j + 1))
                grid[i - 1][j + 1] = 0
        if i > 0: # up
            if grid[i - 1][j] == 1:
                stack.append((i - 1, j))
                grid[i - 1][j] = 0
                


# m = int(input())
# n = int(input())

m = len(grid)
n = len(grid[0])

# grid = []

# get grid

# for i in range(m):
#     grid.append([int(x) for x in input().strip().split()])

regions = []

p(grid)
print()

# iterate through every cell
for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
#             print(f"{(i, j)} --> {grid[i][j]}")
            regions.append(connectedCell(grid, (i, j)))
            p(grid)
            print()
            
print(regions)