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
def LIST(): return list(map(int, input().split()))
# def LIST(): return list(map(str, input().split()))
# def LIST(): return list(input())

sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
L = [LIST() for i in range(N)]

dp = [[0] * 3 for i in range(N)]
# dp_b = [0] * N
# dp_c = [0] * N
dp[0][0] = L[0][0]
dp[0][1] = L[0][1]
dp[0][2] = L[0][2]
for i in range(1, N):
    # dp_a[i+1] = max(dp_a[i]+, )
    # for abc in range(3):
    dp[i][0] = max(dp[i-1][1]+L[i][0], dp[i-1][2]+L[i][0])
    dp[i][1] = max(dp[i-1][2]+L[i][1], dp[i-1][0]+L[i][1])
    dp[i][2] = max(dp[i-1][0]+L[i][2], dp[i-1][1]+L[i][2])

ans = 0
for i in range(3):
    if ans < dp[N-1][i]:
        ans = dp[N-1][i]
print(ans)

