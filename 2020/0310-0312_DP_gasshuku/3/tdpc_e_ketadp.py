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

D = INT()
N = INT()
S = str(N)
L = len(S)

# sum_max = L * 9
# k = 0 Nと一致
# k = 1 Nより小さい
# j 総和で割ったあまり
dp = [[[0] * (1+1) for j in range(D+1)] for i in range(L+1)]

dp[0][0][0] = 1

for i in range(L):
    for j in range(0, D):
        for k in range(2):
            nd = int(S[i])
            for d in range(10):
                ni, nj, nk = i + 1, (j + d) % D, k
                # 今の所Nと一緒
                if k == 0:
                    if d > nd:
                        continue
                    if d == nd:
                        nk = 0
                    if d < nd:
                        nk = 1
                dp[ni][nj][nk] += dp[i][j][k] % mod
ans = (dp[L][0][0] + dp[L][0][1] - 1) % mod
print(ans)
