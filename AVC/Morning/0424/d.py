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

H, W = MAP()
N = INT()
A = LIST()
i = 0
C = [[0] * W for i in range(H)]
k = 0
cnt = 0
for h in range(H):
    if h % 2 == 0:
        for w in range(W):
            C[h][w] = k + 1
            A[k] -= 1
            if A[k] == 0:
                k += 1
    else:
        for w in range(W-1, -1, -1):
            C[h][w] = k + 1
            A[k] -= 1
            if A[k] == 0:
                k += 1

for c in C:
    print(*c, end="\n")
