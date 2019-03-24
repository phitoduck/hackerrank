#!/bin/python3

import math
import os
import random
import re
import sys

def round_pow_2(n):
    start = 1
    num_shifts = 0
    
    while (start < n):
        start <<= 1
        num_shifts += 1
        
    return 1 << num_shifts - 1

def is_pow_2(n):
    num_bits = len(bin(n)) - 2
    mask = 1 << num_bits - 1
    return mask == n

# Complete the counterGame function below.
def counterGame(n):
    
    num_turns = 0
    
    while n > 1:
        if is_pow_2(n):
            n >>= 1
        else:
            n -= round_pow_2(n)
            
        num_turns += 1
        
    return ("Richard" if num_turns % 2 == 0 else "Louise")

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        print(counterGame(n))
