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
mod = 998244353

N, K = MAP()
L = [LIST() for i in range(K)]
# s = set(L[0])
L_l = []
for a, b in L:
    L_l.append(a)
    L_l.append(b)
# print(s)
s = list(set(L_l))
dp = [[0] * N for i in range(len(s)+1)]
print(s)
dp[0][0] = 1

for i in range(len(s)):
    for j in range(0, N):
        # dp[i+1][j] = max(dp[i+1][j+])
        dp[i+1][j+s[i]] = max(dp[i][j]+1, dp[i][j])
print(dp)



