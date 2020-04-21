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

N, W = MAP()
L = [LIST() for i in range(N)]
v_l = []
w_l = []
for v, w in L:
    v_l.append(v)
    w_l.append(w)
V_max = sum(v_l)
# print(V_max)
dp = [[INF] * (V_max + 1) for i in range(N + 1)]
dp[0][0] = 0

for i in range(1, N+1):
    # ココ絶対始め0にする．
    for j in range(0, V_max+1):
        v, w = L[i-1]
        # use
        if j - v >= 0:
            dp[i][j] = min(dp[i-1][j-v] + w, dp[i][j])
        dp[i][j] = min(dp[i-1][j], dp[i][j])


for j in range(V_max, -1, -1):
    if dp[N][j] <= W:
        print(j)
        exit()
