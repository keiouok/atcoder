import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left, bisect_right

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))

sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

X, Y, Z, K = MAP()
A = LIST()
B = LIST()
C = LIST()
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

V = []
for i in range(X):
    for j in range(Y):
        for k in range(Z):
            if (i+1) * (j+1) * (k+1) <= K:
                V.append(A[i]+B[j]+C[k])
            else:
                break

V.sort(reverse=True)

for i in range(K):
    print(V[i])