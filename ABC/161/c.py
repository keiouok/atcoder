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

N, K = MAP()

if N <= K:
    print(min(K-N, N))
# elif K == 1:
#     print(0)
else:
    print(min(N % K, K - N % K))
    # a = N // K
    # b = ceil(N / K)
    # c = N % K
    # print(a, b, c)
    # print(abs(c-K), abs(c))

    # x = N // (N - K)
    # y = x + 1
    # z = x - 1
    # print(x, y, z)
    # a = N - x * (N-K)
    # b = N - y * (N-K)
    # c = N - z * (N-K)
    # print(a, b, c)
    # ans = min(abs(a), abs(b), abs(c))
    # print(ans)

# if N >= K:
#     ans = min(abs(a), abs(b))
# # K > N:
# else:
#     ans = min(K-N, N)
# print(ans)
