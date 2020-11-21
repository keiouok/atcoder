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

N, K = MAP()
T = [LIST() for i in range(N)]

A = [i+1 for i in range(N-1)]
L = list(permutations(A, N-1))
# print(L)
ans = 0
for l in L:
    cnt = 0
    dist = 0
    for y in l:
        if cnt == 0:
            # first
            dist += T[0][y]
            ny = y
            cnt += 1
        else:
            dist += T[ny][y]
            ny = y
    dist += T[y][0]
    # print(dist)
    if dist == K:
        ans += 1
print(ans)