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

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

H, W = MAP()
C = [input() for i in range(H)]
C = ["#"*(W+2)] + ["#"+C[i]+"#" for i in range(H)] + ["#"*(W+2)]
for h in range(H+2):
    for w in range(W+2):
        if C[h][w] == "s":
            sx, sy = w, h
        if C[h][w] == "g":
            gx, gy = w, h

visited = [[False] * (W + 2) for i in range(H + 2)]
visited[sy][sx] = True
# print(sy, sx)
# print(visited)
def dfs(cx, cy):
    # if cx == gx and cy == gy:        
    # C[cy][cx] = "#"
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        # print(nx, ny)
        if C[ny][nx]!= "#" and visited[ny][nx] == False:
            visited[ny][nx] = True
            dfs(nx, ny)

    # return False
dfs(sx, sy)
print("Yes" if visited[gy][gx] else "No")
# if dfs(sx, sy) == True:
#     print("Yes")
# else:
#     print("No")
