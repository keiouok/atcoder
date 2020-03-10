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
NG = [INT() for i in range(3)]

dp = [INF] * (N+1)
# 0手
dp[N] = 0
# k に辿り着くまでに最大何手必要か
for i in range(N, -1, -1):
    if i in NG:
        continue
    for j in range(1, 4):
        if i - j >= 0:
            dp[i-j] = min(dp[i] + 1, dp[i-j])
        # 必ず1, 2, 3で引くのでこれはなし
        # dp[i-j] = min(dp[i], dp[i-j])
# print(dp[0])
if dp[0] <= 100:
    print("YES")
else:
    print("NO")


