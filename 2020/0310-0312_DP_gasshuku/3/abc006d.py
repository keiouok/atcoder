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
A = [INT() for i in range(N)]
C = []
for a in A:
    C.append(int(a))

D = sorted(C)

ans = 0
# for i in range(N-1):
#     if C[i+1] >= C[i]:
#         continue
#     else:
#         ans += 1
# print(ans)
dp = [[INF] * (len(C)+1) for i in range(len(C)+1)]
dp[0][0] = 0



for i in range(len(C)):
    for j in range(len(D)):
        if C[i] == D[j]:
            dp[i+1][j+1] = min(dp[i][j], dp[i][j+1]+1, dp[i+1][j]+1)
        else:
            dp[i+1][j+1] = min(dp[i][j]+1, dp[i][j+1]+1, dp[i+1][j] + 1)

print(dp[len(C)][len(D)])

