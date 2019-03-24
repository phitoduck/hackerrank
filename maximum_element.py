from collections import deque
import math

n = int(input())

class stack:
    def __init__(self):
        self.stack = deque()
        self.maxes = deque()
        self.max = -math.inf
    
    def push(self, x):
        self.stack.appendleft(x)
        
        if (len(self.maxes) > 0):
            maxtop = self.maxes.popleft()
            self.maxes.appendleft(maxtop)
        else:
            maxtop = x
            
        if len(self.maxes) == 0:
            self.maxes.appendleft(maxtop)
        elif x > maxtop:
            self.maxes.appendleft(x)
        else:
            self.maxes.appendleft(maxtop)
        
    def delete(self):
        self.stack.popleft()
        self.maxes.popleft()
        
    def print_max(self):
        maxtop = self.maxes.popleft()
        self.maxes.appendleft(maxtop)
        print(maxtop)
        
        
stack = stack()

for i in range(n):
    args = [int(x) for x in input().strip().split()]
    
    # print(stack.maxes)
    # print(stack.stack)
    
    if args[0] == 1:
        stack.push(args[1])
    elif args[0] == 2:
        stack.delete()
    elif args[0] == 3:
        stack.print_max()
