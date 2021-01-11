import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
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

N, C = MAP()
L = [LIST() for i in range(N)]

info = set()

for a, b, c in L:
    info.add(a)
    info.add(b+1)

info = sorted(info)
M = len(info)

dates = {date:idx for idx, date in enumerate(info)}

imos = [0] * (M + 1)
cur_imos = [0] * (M + 1)

for a, b, c in L:
    a_i = dates[a]
    b_i = dates[b+1]
    imos[a_i] += c
    imos[b_i] -= c

for i in range(M):
    cur_imos[i+1] = cur_imos[i] + imos[i]

ans = 0
for i in range(M-1):
    tmp = min(cur_imos[i+1], C) * (info[i+1] - info[i])
    ans += tmp
print(ans)