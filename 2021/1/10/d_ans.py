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

info_set = set()

for a, b, c in L:
    info_set.add(a)
    info_set.add(b+1)

dates = sorted(info_set)
# print(dates)
# 本当に日付：圧縮する対象の座標
dates_d = {date:idx for idx, date in enumerate(dates)}
# print(dates_d)
M = len(dates)

imos = [0] * (M + 1)

for a, b, c in L:
    # a, b : datesのkey
    a_idx = dates_d[a]
    b_idx = dates_d[b+1]
    imos[a_idx] += c
    imos[b_idx] -= c

cum_sum = [0] * (M + 1)

for i in range(M):
    cum_sum[i+1] = cum_sum[i] + imos[i]
    # imos[i+1] = imos[i+1] + imos[i]

ans = 0

for i in range(M - 1):
    # add = min(imos[i+1], C) * (dates[i+1] - dates[i])
    add = min(cum_sum[i+1], C) * (dates[i+1] - dates[i])
    ans += add
print(ans)
