# はじめて自力でできた
# 20200315 19:51-20:10
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
C = [input() for i in range(H)]

for i in range(H):
    for j in range(W):
        if C[i][j] == "s":
            sx = j
            sy = i
for i in range(H):
    for j in range(W):
        if C[i][j] == "g":
            gx = j
            gy = i

s = [(sy, sx)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[False] * W for i in range(H)]
visited[sy][sx] = True
def dfs():
    while s:
        y, x = s.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < W and 0 <= ny < H and visited[ny][nx] == False and C[ny][nx] != "#":
                if C[ny][nx] == "g":
                    print("Yes")
                    exit()
                # C[ny][nx] = "#"
                visited[ny][nx] = True
                s.append((ny, nx))
    print("No")
dfs()


