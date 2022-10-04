#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    l = []
    while n >= 1:
        if n%2 == 0:
            l.append('0')
            n = n/2
        else:
            l.append('1')
            n = (n-1)/2
    l = ''.join(l)
    l_new = l.split('0')
    arr = [len(item) for item in l_new]
    consecutive_of_1 = max(arr)
    print(consecutive_of_1)
