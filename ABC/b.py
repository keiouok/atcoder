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
A = [LIST() for i in range(N)]
C = [LIST() for i in range(M)]
L = []
for i in range(N):
    index = 0
    mi = INF
    for j in range(M):
        a, b = A[i][0], A[i][1]
        c, d = C[j][0], C[j][1]
        m = abs(a - c) + abs(b - d)
        if mi > min(mi, m):
            mi = min(mi, m)
            index = j
    L.append(index)
for l in L:
    print(l+1)



