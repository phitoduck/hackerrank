"""

Eric Riddoch
Volume II
HW 3.2 # 10) Queue with two stacks

This algorithm does the following:
1) Create one stack for inserting and one stack for popping
2) When we push an element, insert it onto the insertion stack
3) When we pop an element, do one of two things:
    a) If popping stack is not empty, pop ∈ O(1) in this case
        (This stack is always in order)
    b) If the popping stack is empty, pop every element from
        the insertion stack onto the popping stack, except
        pop the last element. Worst case pop ∈ O(n)
4) When we want to insert, simply insert onto insertion stack.
    push() ∈ O(1) always.

"""

def flip(s1, s2):
    k = len(s1)
    for i in range(k):
        s2.append(s1.pop())

class Queue:
    def __init__(self):
        self.on = deque()
        self.off = deque()
    
    def enqueue(self, a):
        self.on.append(a)
        
    def dequeue(self):
        if (len(self.off) == 0):
            flip(self.on, self.off)
            self.off.pop()
        else:
            self.off.pop()
            
    def __str__(self):
        if (len(self.off) != 0):
            return str(self.off[ len(self.off) - 1 ])
        else:
            return str(self.on[0])
            
# Main
            
n = int(input())
s1 = deque()
s2 = deque()

Q = Queue()

# if items are in stack one, in_order = False
#    We are free to push items onto s1 for enqueue in this state
# if items are in stack two, in_order = True
#    We are free to dequeue items by popping off the top of stack two

for i in range(n):    
    
    nums = input().split()
    nums[0] = int(nums[0])
    
    if len(nums) == 2:
        # enqueue
        Q.enqueue(nums[1])
    elif nums[0] == 2:
        # dequeue
        Q.dequeue()
    elif nums[0] == 3:
        print(str(Q))