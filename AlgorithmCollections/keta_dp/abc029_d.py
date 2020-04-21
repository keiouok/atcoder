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
L = len(n)
K = 10
# dp[i][j][k]
# j その地点で持っている1の数
#
dp = [[[0] * 2 for i in range(K)] for i in range(L+1)]
# K+1のところKにした

dp[0][0][0] = 1

for i in range(L):
    for j in range(K):
        for k in range(2):
            nd = int(n[i])
            for d in range(10):
                ni = i + 1
                nj = j
                nk = k
                
                if d == 1:
                    nj += 1
                # 10 ** 9 より大きくなることはない
                if nj > 9:
                    continue
                #    
                if k == 0:
                    if d == nd:
                        nk = 0
                    if d > nd:
                        continue
                    if d < nd:
                        nk = 1

                dp[ni][nj][nk] += dp[i][j][k]
# ans = dp[L][K][0] + dp[L][K][1]

ans = 0
# iをかけた(?)
for i in range(1, 10):
    ans += i * (dp[L][i][0] + dp[L][i][1])
# print(dp)
print(ans)