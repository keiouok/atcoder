import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, floor
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

N, x = MAP()
A = LIST()

# Who are you?


#B = [0] * (N - 1)
B = []
for i in range(N-1):
    B.append(A[i+1] + A[i])

B.append(0)
print(B)
pre = sum(A)
for i in range(N - 1):
    if B[i] > x:
        if A[i+1] >= B[i] - x:
            A[i+1] -= B[i] - x
            B[i] = x
            B[i+1] -= B[i] - x
        else:
            B[i] -= A[i+1] + x
            A[i+1] = 0
            A[i] -= B[i] - x
            #B[i+1] -= B[i] - x
after = sum(A)
print(pre-after)
print(A)
print(B)
