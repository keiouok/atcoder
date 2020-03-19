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
S = input()
T = [input() for i in range(N)]

M = len(S)
dp = [0] * (M+1)
#  for i in range(N+1)]
# dp[0][0] = 1
dp[0] = 1
for i in range(M):
    for j in range(N):
        r = len(T[j])
        # T[j]と呪文の見ているところが重なるなら
        if S[i:i+r] == T[j]:
            dp[i+r] = (dp[i+r]+dp[i]) % mod

print(dp[M])

