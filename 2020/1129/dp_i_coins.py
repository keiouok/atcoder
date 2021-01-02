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
def LIST(): return list(map(float, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
p = LIST()
# N <= 2999
dp = [[0] * (3100) for i in range(3100)]
dp[0][0] = 1.0

for i in range(N):
    for j in range(i+1):
        # 次のコインが表の時
        dp[i+1][j+1] += dp[i][j] * p[i]
        # 次のコインが裏の時
        dp[i+1][j] += dp[i][j] * (1 - p[i])

ans = 0
# 1 - 50 だと，25 - 50, 1 - 49 だと， 25 - 49までが0.5以上の領域．そこの確率の和を出す
for j in range(N // 2 + 1, N + 1):
    ans += dp[N][j]
print(ans)