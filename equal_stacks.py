#!/bin/python3

import os
import sys

from collections import deque

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    s1 = deque(h1)
    s2 = deque(h2)
    s3 = deque(h3)
    
    sum1 = sum(s1)
    sum2 = sum(s2)
    sum3 = sum(s3)
    
    # remove from tallest stack until the two are equal
    while sum1 != sum2 or sum2 != sum3:
        
        # pop from tallest of first two
        max_sum = max(sum1, sum2)
        while (sum1 != sum2):
            if (sum1 > sum2):
                sum1 -= s1.popleft()
            else:
                sum2 -= s2.popleft()
                
        # pop from tallest of second two
        max_sum = max(sum2, sum3)
        while (sum2 != sum3):
            if sum2 > sum3:
                sum2 -= s2.popleft()
            else:
                sum3 -= s3.popleft()
                
    return sum1
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
