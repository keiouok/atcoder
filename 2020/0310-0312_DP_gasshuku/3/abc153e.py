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

H, N = MAP()
L = [LIST() for i in range(N)]
A = []
B = []
for a, b in L:
    A.append(a)
    B.append(b)

v = H + max(A)

dp = [[INF] * (v + 1) for i in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(v):
        if j-A[i] >= 0:
            dp[i+1][j] = min(dp[i+1][j-A[i]]+B[i], dp[i][j])
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

print(min(dp[N][H:]))

# for i in range(1, N+1):
#     for j in range(1, v+1):
#         if j-A[i-1] >= 0:
#             # i
#             dp[i][j] = min(dp[i-1][j-A[i-1]]+B[i-1], dp[i][j])
#         dp[i][j] = min(dp[i-1][j], dp[i][j])

# print(dp[N][H:])


