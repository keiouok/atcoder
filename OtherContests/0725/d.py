import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left, bisect_right

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

have = 1000

# dp = [[0] * (200 * 80 + 1) for i in range(20+1)]
dp = [[0] * (160 + 1) for i in range(N + 1)]

for i in range(160 + 1):
    dp[0][i] = 1000

for i in range(N):
    for j in range(160):
        # i + 1日目の株の金
        one = A[i]
        # 株を列長さ分かった時の株の値段全部
        buy = one * j
        sold = one * 
        # 変動後所持金
        before_have = dp[i][j]
        after_have = max(0, dp[i][j] - buy)
        dp[i+1][j+1] = max(before_have, after_have)
print(max(dp[i+1]))
print(dp)


