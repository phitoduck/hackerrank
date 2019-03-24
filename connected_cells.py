# find the largest number of connected cells in a grid
# where connected is defined as adjacent horizontally, 
# vertically, and diagonally

from collections import deque
    
def is_valid_move(move, m, n):
    return move[0] in range(m) and move[1] in range(n)

def add_tuples(tup1, tup2):
    return tup1[0] + tup2[0], tup1[1] + tup2[1]

def print_grid(grid):
    for row in grid:
        print( " ".join( list(map(str, row)) ) )
    print()
    
def depth_search(grid, row, col, m, n):
    
    moves = [
        (0, 1), (1, 0), (0, -1), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    
    stack = deque([ (row, col) ])
    
    island_size = 0
    while len(stack) > 0:
        
        loc = stack.popleft()
        island_size += 1
        
        # set visited value to 0
        grid[loc[0]][loc[1]] = 0
        
        # check in each direction
        for move in moves:
            # calculate next move
            next_move = add_tuples( loc, move )
            # only move if we're on the grid
            if is_valid_move(next_move, m, n):
                # append nonzero locations
                if grid[next_move[0]][next_move[1]] != 0:
                    grid[next_move[0]][next_move[1]] = 0
                    stack.appendleft( next_move )
                    
    return island_size
    
    

if __name__ == "__main__":
    m = int(input().strip())
    n = int(input().strip())
    grid = [ 
        [int(x) for x in input().strip().split()] for i in range(m) 
    ]
    
    # loop through grid
    island_sizes = list([0])
    for row in range(m):
        for col in range(n):
            # depth first search on values that are not zero
            if grid[row][col] != 0:
                result = depth_search(grid, row, col, m, n)
                if type(result) == int:
                    island_sizes.append(result)
    
    print(max(island_sizes))
                
    



