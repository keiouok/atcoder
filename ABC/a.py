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

m, d = MAP()

# print(d1)
# print(l)
count = 0
for i in range(1, m+1):
    for j in range(1, d+1):
        if j >= 20:
            d1 = j % 10
            d10 = j // 10
            # print(d1)

            if d1 >= 2:
                # print("d1:"d1)
                
                if d1 * d10 == i:
                    count += 1

        # if d1 >= 2:
        #     if d10 >= 2:
        #         if d1 * d10 == m:
        #             count += 1


print(count)