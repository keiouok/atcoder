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

N = INT()
S = input()
T = "atcoder"
lent = len(T)
# T = "chokudai"
# N = len(S)

dp = [[0] * (lent + 1) for i in range(N + 1)]

dp[0][0] = 1

for i in range(N + 1):
    for j in range(lent + 1):
        if j == 0:
            dp[i][0] = 1
        elif i == 0:
            dp[0][j] = 0
        elif S[i - 1] == T[j - 1]:
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % mod
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][lent])