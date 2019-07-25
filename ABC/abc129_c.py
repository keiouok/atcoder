
import sys, re
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

N, M = MAP()
A = [INT() for _ in range(M)]

b = [0] * (N + 2)
# 壊れているところが1
for i in A:
    b[i] = 1

dp = [0] * (N + 2)
# for i in range():

dp[0] = 1

if b[1] == 1:
    # あなあいてるのでそのルートは考えられない
    dp[1] = 0
else:
    dp[1] = 1

for i in range(2, N + 1):
    if b[i] == 1:
        dp[i] = 0
    else:
        dp[i] = dp[i-1] + dp[i-2]

ans = dp[N] % mod
print(ans)
