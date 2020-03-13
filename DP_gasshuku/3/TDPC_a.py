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

N = INT()
A = LIST()

dp = [[0] * 100001 for i in range(N+1)]
# 0ketame
dp[0][0] = 1

for i in range(N):
    # use
    for j in range(0, 100001):
        if j - A[i] >= 0:
            dp[i+1][j] = max(dp[i][j-A[i]], dp[i+1][j])
        dp[i+1][j] = max(dp[i][j], dp[i+1][j])
ans = 0
# print()
# print(dp[3][2])
# for i in range(N+1):
for j in range(100001):
    if dp[N][j] != 0:
        ans += 1

print(ans)