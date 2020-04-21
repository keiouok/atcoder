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

N, K = MAP()
h = LIST()

dp = [INF] * N
dp[0] = 0
for i in range(N):
    for j in range(1, K+1):
        if i + j < N:
            dp[i+j] = min(dp[i] + abs(h[i] - h[i+j]), dp[i+j])
        # if dp[i] >= dp[i-j] + abs(h[i]-h[i-j]):
        #     dp[i] = dp[i-j] + abs(h[i]-h[i-j])
print(dp[-1])
