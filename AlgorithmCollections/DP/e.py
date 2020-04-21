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
def LIST(): return list(map(int, input().split()))
# def LIST(): return list(map(str, input().split()))
# def LIST(): return list(input())

sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, W = MAP()
L = [LIST() for _ in range(N)]

V = 0
# sum_v = 0
for w, v in L:
    V += v

dp = [[INF] * (V+1) for i in range(N+1)]
dp[0][0] = 0

# V = sum(v)
for i in range(1, N+1):
    for j in range(0, V+1):
        # j，1スタートだと16,0スタートだと17になる
        w = L[i-1][0]
        v = L[i-1][1]
        if j - v >= 0:
            dp[i][j] = min(dp[i-1][j - v] + w, dp[i][j])
        dp[i][j] = min(dp[i][j], dp[i-1][j])

# ans = 0
for sum_v in range(V+1):
    # print(dp[N][sum_v])
    # print(dp)
    if dp[N][sum_v] <= W:
        ans = sum_v
print(ans)
