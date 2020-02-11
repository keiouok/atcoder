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

n = input()
k = INT()
L = len(n)

# dp[L][k][2]

# k = 0 nと一致
# k = 1 nより小さい
dp = [[[0] * 2 for i in range(4)] for j in range(L+1)]
dp[0][0][0] = 1
for i in range(L):
    for j in range(4):
        for k in range(2):
            nd = int(n[i])
            # print(nd)
            for d in range(10):
                ni = i + 1
                nj = j
                nk = k
                if d != 0:
                    nj += 1
                if nj > k:
                    continue
                if k == 0:
                    if d > nd:
                        continue
                    # if d == nd:
                    #     nk = 0
                    if d < nd:
                        nk = 1
                # print(ni, nj, nk)
                dp[ni][nj][nk] += dp[i][j][k]

ans = dp[L][k][0] + dp[L][k][1]
print(ans)
            
            
