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

N, M = MAP()
L = [LIST() for i in range(M)]

num = [1] * N
red = [False] * N
red[0] = True

for a, b in L:
    if num[a-1] == 0:
        # 水がない
        red[a-1] = False
        continue
    else:
        num[b-1] += 1
        num[a-1] -= 1
        red[b-1] = red[b-1] or red[a-1]
        if num[a-1] == 0:
            red[a-1] = False
    
print(sum(red))
# print(sum(num))

