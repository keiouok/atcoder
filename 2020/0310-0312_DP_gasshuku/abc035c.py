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

N, Q = MAP()
L = [LIST() for i in range(Q)]

imos = [0] * (N+1)
for l, r in L:
    imos[l-1] += 1
    imos[r] += -1
    #plus = [0] * (l - 1) + [1] * (r - l + 1) + [0] * (N - r)
    #print(new)
    #for i in range(N):
    #    new[i] ^= plus[i]
for i in range(N):
    imos[i+1] += imos[i]
    if imos[i] % 2 == 0:
        imos[i] = 0
    else:
        imos[i] = 1
imos.pop()

print(*imos, sep="")

