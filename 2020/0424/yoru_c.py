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
A = LIST()
C = Counter(A)
# print(C)
# combinations()
al = 0
for ball, num in C.items():
    al += num * (num - 1) // 2
# print(al)
for a in A:
    ball = a
    num = C[a]
    ans = al - C[a] * (C[a] - 1) // 2 + (C[a] - 1) * (C[a] - 2) // 2
    print(ans)

# for a in A:
#     c[a]