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
sy, sx = MAP()
gy, gx = MAP()
C = [input() for i in range(H)]

sy = sy - 1
sx = sx - 1
gy = gy - 1
gx = gx - 1

q = deque([(sy, sx)])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[False] * W for i in range(H)]
# visited[sy][sx] = True
visited[sy][sx] = 0
def bfs():
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < H and 0 <= nx < W and visited[ny][nx] == False and C[ny][nx] != "#":
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))
                # visited[ny][nx] = True
                if gx == nx and gy == ny:
                    print(visited[ny][nx])
                    exit()
            
bfs()




