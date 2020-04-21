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

N, M = MAP()            
A = [INT() for i in range(M)]

dp = [INF] * (N + 1)
dp[0] = 1
dp[1] = 1
for a in A:
    dp[a] = 0

for i in range(1, N+1):
    if dp[i] == 0:
        continue
    if i-2 >= 0:
        dp[i] = min(dp[i], dp[i-1] + dp[i-2])
    elif i - 1 >= 0:
        dp[i] = min(dp[i], dp[i-1])
# print(dp)
print(dp[N] % mod)
    




