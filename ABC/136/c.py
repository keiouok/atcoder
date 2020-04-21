import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))

sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

n = INT()
h = LIST()


table = [0] * n
h[0] = h[0] - 1

while(1):
    h_def = h
    for i in range(n-1):
        if h[i]>h[i+1]:
            h[i] = h[i]-1
            table[i] += 1
    for i in range(n):
        if table[i] > 1:
            print("No")
            exit()


    # print(h_def)
    # print(h)
    count = 0
    for i in range(n-1):
        if h[i] <= h[i+1]:
            count += 1
    # print(count)

    if count == n-1:
        print("Yes")
        exit()

        
        # if h[i] > h[i+1]:
        #     flag = True
        

    # if h_def == h:
    #     print("Yes")
    #     exit()
    

#     # elif h[i]
# print(h)
# flag = True    
# for i in range(n-1):
#     if h[i]>h[i+1]:
#         flag = False

# if flag == True:
#     print("Yes")
# else:
#     print("No")
