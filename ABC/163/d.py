import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from heapq import heapify, heappop, heappush

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, K = MAP()

ans = 0
for k in range(K, N + 2):
    # k個足してできる最大の整数
    # 大きい順にk個選べばよい
    # N + (N - 1) + ... + (N - k + 1)
    # = (0+1+...+N) - (0+1+...+(N-k)) = B
    B = N * (N + 1) // 2 - (N - k) * (N - k + 1) // 2
    # 最小の整数は小さい順にk個選べばよい
    # 0 + 1 + ... + (k-1)
    A = (k - 1) * k // 2
    # k個足してできる整数の数
    ans += (B - A + 1)
print(ans % mod)