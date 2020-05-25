import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from heapq import heapify, heappop, heappush
 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
L = [LIST() for i in range(N)]

import itertools
l = [i for i in range(N)] #生成する数字
bit = list(permutations(l))
# print(bit)
cnt = 0
ans = 0
s = 0
for t in bit:
    # s = 0
    # print(t)
    for i in range(len(t)-1):
        # print(i)
        a, b = L[t[i]][0], L[t[i]][1]
        c, d = L[t[i+1]][0], L[t[i+1]][1]
        s += sqrt((a - c) ** 2 + (b - d) ** 2)
    # print(s)
    # ans += s
    # s = 0

ans = s / len(bit)
print(ans)