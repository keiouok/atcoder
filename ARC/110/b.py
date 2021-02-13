import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

B, C = MAP()

up_max = C // 1
down_max = C // 2 # only down
# print(up_max, down_max)

# print(B - down_max + 1)
# minu = B - down_max 
# print(minu)

# BがmunusならこれでOK
# マイナス部分の反射
# if minu <= -1:
# minu = B - down_max
# print(minu)
if B < 0:
    if C % 2 == 0:
        minu = B - down_max
        ref = abs(minu) * 2
    # 一個残す
    elif C % 2 == 1:
        minu = B - down_max - 1
        ref = abs(minu) * 2
elif B == 0:
    if C % 2 == 0:
        minu = B - down_max
        ref = abs(minu) * 2
    # 一個残す
    elif C % 2 == 1:
        minu = B - down_max - 1
        ref = abs(minu) * 2
elif B > 0:
    # minu = B - down_max
    # if minu <= 0:
    # print(minu)
    # abs(minu)
    if C % 2 == 0:
        minu = - B - down_max
        ref = abs(minu) * 2
    # 一個残す
    elif C % 2 == 1:
        minu = - B - down_max
        ref = abs(minu) * 2
print(ref)




