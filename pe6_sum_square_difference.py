# Project Euler #6, Sum Square Difference

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    sum_regular = (n) * (n + 1) / 2
    
    sum_squareds = (n) * (2*n + 1) * (n + 1) / 6
    
    print(int(sum_regular**2 - sum_squareds))
