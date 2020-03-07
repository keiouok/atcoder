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

dp = [[0] * (W+1) for i in range(N+1)]
# for w, v in L:
for i in range(1, W+1):
    for j in range(1, N+1):
        w = L[j-1][0]
        v = L[j-1][1]
        if i - w >= 0: 
            dp[j][i] = max(dp[j-1][i-w] + v, dp[j][i])
        dp[j][i] = max(dp[j][i], dp[j-1][i])

print(dp[N][W])


