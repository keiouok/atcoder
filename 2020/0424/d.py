import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from heapq import heapify, heappop, heappush
 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

H, W, K, V = MAP()
A = [LIST() for i in range(H)]
ruiseki = [[0] * (W + 1) for h in range(H + 1)]

for h in range(H):
    for w in range(W):
        ruiseki[h+1][w+1] = A[h][w] + K

for h in range(H+1):
    for w in range(W):
        ruiseki[h][w+1] = ruiseki[h][w] + ruiseki[h][w+1] 

for w in range(W+1):
    for h in range(H):
        ruiseki[h+1][w] = ruiseki[h+1][w] + ruiseki[h][w] 

ans = 0
s = 0
for h1 in range(H+1):
    for h2 in range(h1+1, H+1):
        for w1 in range(W+1):
            dy = h2 - h1
            # for w2 in range(w1+1, W+1):
            for w2 in range(s//dy + w1, W+1):
                tmp = ruiseki[h2][w2] + ruiseki[h1][w1] - ruiseki[h2][w1] - ruiseki[h1][w2]
                if tmp <= V:
                    # if ans <= tmp:
                    #     ans = tmp
                    s = max((h2 - h1) * (w2 - w1), s)
print(s)