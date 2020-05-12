import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from heapq import heapify, heappop, heappush
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
C = [[0] * W for i in range(H)]
num = 0
for h in range(H):
    if h % 2 == 0:
        for w in range(W):
            if A[num] > 0:
                A[num] -= 1
            else:
                num += 1
                A[num] -= 1
            C[h][w] = num + 1
    else:
        for w in range(W-1, -1, -1):
            if A[num] > 0:
                # C[h][w] = num + 1
                A[num] -= 1
            else:
                num += 1
                A[num] -= 1
            C[h][w] = num + 1

for c in C:
    print(*c, end="\n")    
