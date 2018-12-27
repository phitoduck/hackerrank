# Pacman BFS Algorithm

from collections import deque
from math import inf

# Awesome way to make a graph
def make_graph(grid, rows, cols):
    graph = dict()
    
    moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    valid = ['-', 'P', '.']
    
    for i in range(rows):
        for j in range(cols):
            
            if grid[i][j] not in valid:
                continue
                
            loc = (i, j)
            
            # initialize location neighbors to empty list
            graph[loc] = []
            
            # Check UP, DOWN, LEFT, RIGHT
            for move in moves:
                if i > 0 and i < rows and j > 0 and j < cols:
                    check = (i + move[0], j + move[1])
                                        
                    if grid[check[0]][check[1]] in valid:
                        graph[loc].append( check )
            
    return graph

# Normal way to make a graph
def make_graph_not_used(grid, rows, cols):
    graph = dict()
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '%':
                continue
                
            loc = (i, j)
            valid = ['-', 'P', '.']
            
            # initialize location neighbors to empty list
            graph[loc] = []
            
            if i > 0: # UP
                if grid[i - 1][j] in valid:
                    graph[loc].append( (i - 1, j) ) 
            if j > 0: # LEFT
                if grid[i][j - 1] in valid:
                    graph[loc].append( (i, j - 1) )
            if j < cols: # RIGHT
                if grid[i][j + 1] in valid:
                    graph[loc].append( (i, j + 1) )
            if i < rows: # DOWN
                if grid[i + 1][j] in valid:
                    graph[loc].append( (i + 1, j) )
                    
    return graph

# BFS
def find_food(graph, pacman, food):

    explorePath = []
    pathToFood = []
    
    visited = set()
    # visited.add(pacman)
    
    Q = deque()
    Q.append([pacman])
    # visited.add(pacman)
    
    # pop locations until the queue is empty
    while len(Q) > 0:
        
        # get the location in line
        path = Q.popleft()

        if path[-1] not in visited:
            explorePath.append(path[-1])
            
        # push next locations
        for node in graph[path[-1]]:
            
            if node not in visited and node not in path:
                visited.add(node)
            
                explorePath.append(node)
                Q.append(path + [node])
                
                # did we find it?
                if node == food:
                    return path + [node], explorePath

    print("Food was not found!")
    return None

###################################
#        SOLVE THE PROBLEM        #
###################################

# Get problem information, store locations as tuples
pacman = list(map(int, input().strip().split()))
pacman = (pacman[0], pacman[1])

food = list(map(int, input().strip().split()))
food = (food[0], food[1])

rows, cols = list(map(int, input().strip().split()))

grid = [[x for x in input()] for _ in range(rows)]

graph = make_graph(grid, rows, cols)
pathToFood, explorePath = find_food(graph, pacman, food)

# Tie it all together and solve
def solve(grid, rows, cols, pacman, food):
    
    print(len(explorePath))
    
    for location in explorePath:
        print(location[0], location[1])
    
    print(len(pathToFood) - 1)
    
    for location in pathToFood:
        print(location[0], location[1])
            
solve(grid, rows, cols, pacman, food)