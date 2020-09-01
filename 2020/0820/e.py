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

H, W, M = MAP()
L = [LIST() for i in range(M)]

yoko = [0] * W
tate = [0] * H
Map = [[0] * W for i in range(H)]

for h, w in L:
    Map[h-1][w-1] = 1

for h in range(H):
    tate[h] = sum(Map[h])

for w in range(W):
    for h in range(H):
        yoko[w] += Map[h][w]

Map2 = [[0] * W for i in range(H)]

ma = 0
for h in range(H):
    for w in range(W):
        if Map[h][w] == 1:
            Map2[h][w] = yoko[w] + tate[h] - 1
            ma = max(Map2[h][w], ma)
        else:
            Map2[h][w] = yoko[w] + tate[h]
            ma = max(Map2[h][w], ma)
print(ma)