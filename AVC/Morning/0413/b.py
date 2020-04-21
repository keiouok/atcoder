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
S = [input() for i in range(H)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            cnt = 0
            for i in range(4):
                if 0 <= h + dy[i] < H and 0 <= w + dx[i] < W:
                    if S[h+dy[i]][w+dx[i]] == "#":
                        cnt += 1
            if cnt == 0:
                print("No")
                exit()
print("Yes")
                