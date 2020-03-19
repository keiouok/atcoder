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

N, T = MAP()
L = [LIST() for i in range(N)]

dp = [[0] * (T) for i in range(N+1)]

L.sort()
for i in range(N):
    for j in range(T):
        if j - L[i][0] >= 0:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j-L[i][0]]+L[i][1])
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
# print(dp[N][T-1])

ans = 0
for k in range(N):
    # k番目を食べずにk-1番目まで食べたT-1秒以下での最大値に，
    # k番目のものをT-1秒目に食べた値の中での最大値
    # 一番いいものを最後に食べる
    ans = max(dp[k][T-1] + L[k][1], ans)
print(ans)



