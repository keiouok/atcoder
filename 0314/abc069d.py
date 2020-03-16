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

H, W = MAP()
N = INT()
A = LIST()
C = [[INF] * W for i in range(H)]

even = 0
num = 0
for i in range(H):
    if even == 0:
        for j in range(W):
            if A[num] > 0:
                C[i][j] = num + 1
                A[num] -= 1
            else:
                num += 1
                C[i][j] = num + 1
                A[num] -= 1

            # for k in range():
        even ^= 1
    else:
        for j in range(W-1, -1, -1):
            if A[num] > 0:
                C[i][j] = num + 1
                A[num] -= 1
            else:
                num += 1
                C[i][j] = num + 1
                A[num] -= 1

        even ^= 1

for c in C:
    print(*c, end="\n")
        # C[i][j]
