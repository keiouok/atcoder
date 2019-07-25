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

N = INT()
h = LIST()
dp = [INF] * N
dp[0] = 0
dp[1] = abs(h[1] - h[0])
# for i in range(2, N):
#     a = abs(dp[i-2] + abs(h[i] - h[i-2]))
#     b = abs(dp[i-1] + abs(h[i] - h[i-1]))
#     dp[i] = min(a, b)
# print(dp[-1])

for i in range(2, N):
    a = dp[i-2] + abs(h[i] - h[i-2])
    b = dp[i-1] + abs(h[i] - h[i-1])
    dp[i] = min(a, b)
print(dp[-1])

