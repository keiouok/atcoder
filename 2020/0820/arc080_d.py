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
C = [[0] * W for i in range(H)]
i = 0
for h in range(H):
    for w in range(W):
        while A[i] == 0:
            i += 1
        if h % 2 == 0:
            # forward
            C[h][w] = i + 1
        else:
            # backward
            C[h][W-w-1] = i + 1
        A[i] -= 1
# print(*[c for c in C], sep="\n")
for c in C:
    print(*c, sep=" ")      
