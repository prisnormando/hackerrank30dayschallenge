#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
max_sum = (arr[0][0] + arr[0][1]+ arr[0][2]) + (arr[1][1]) + (arr[2][0]++ arr[2][1]+ arr[2][2])

for i in range(len(arr)):
    if i >=4:
        continue
    for j in range(len(arr[i])):
        if j>=4:
            continue
        curr_sum = (arr[i][j] + arr[i][j+1]+ arr[i][j+2]) + (arr[i+1][j+1]) + (arr[i+2][j]+ arr[i+2][j+1]+ arr[i+2][j+2])
        if curr_sum > max_sum:
            max_sum = curr_sum

print(max_sum)
