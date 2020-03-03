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

A = LIST()

X = []
Y = []

for i in range(6):
    if i % 2 == 0:
        X.append(A[i])
    else:
        Y.append(A[i])

a = X[1] - X[0]
b = Y[1] - Y[0]
c = X[2] - X[0]
d = Y[2] - Y[0]

print(0.5 * abs(a * d - b * c))
