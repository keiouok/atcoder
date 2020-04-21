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


h, w = MAP()
sy, sx = MAP()
gy, gx = MAP()

sy, sx = sy-1, sx-1
gy, gx = gy-1, gx-1


c = []

for i in range(h):
    c.append(list(input()))
#print(c)

def bfs():
    d = [[INF for i in range(w)] for j in range(h)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    que = deque([])
    que.append((sy, sx))
    d[sy][sx] = 0
    #cx = sx
    #cy = sy
    while que:
        p = que.popleft()
        for i in range(4):
            nx = p[1] + dx[i]
            ny = p[0] + dy[i]
            if 0 <= nx < w and 0 <= ny < h and c[ny][nx] == "." and d[ny][nx] == INF:
                que.append((ny, nx))
                d[ny][nx] = d[p[0]][p[1]] + 1
            if ny == gy and nx == gx:
                return d[ny][nx]

        

print(bfs())
