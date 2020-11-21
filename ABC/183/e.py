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
mod = 10 ** 9 + 7

H, W = MAP()
S = [input() for i in range(H)]
dp = [[0] * W for i in range(H)]
X = [[0] * W for i in range(H)]
Y = [[0] * W for i in range(H)]
Z = [[0] * W for i in range(H)]


# for i in range(H):
#     for j in range(W):
#         if S[i][j] == "#":
#             X[i][j] = 0
#             Y[i][j] = 0
#             Z[i][j] = 0
#             dp[i][j] = 0
# X 右
# for i in range(H):
#     for j in range(1, W):
#         if S[i][j] == ".":
#             X[i][j] += X[i][j-1]
# # Y 下
# for i in range(1, H):
#     for j in range(W):
#         if S[i][j] == ".":
#             Y[i][j] += Y[i-1][j]
# # Z 斜め
# for i in range(H):
#     for j in range(W):
#         if S[i][j] == ".":
#             Z[i][j] += Z[i-1][j-1]

dp[0][0] = 1
# X[0][0] = 1
# Y[0][0] = 1
# Z[0][0] = 1

for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            continue
        elif S[i][j] == "#":
            continue
        if j > 0:
            X[i][j] = X[i][j-1] + dp[i][j-1]
        if i > 0:
            Y[i][j] = Y[i-1][i] + dp[i-1][j]
        if i > 0 and j > 0:
            Z[i][j] = Z[i-1][j-1] + dp[i-1][j-1]
        dp[i][j] += X[i][j] + Y[i][j] + Z[i][j]
        dp[i][j] %= mod
print(dp[-1][-1])