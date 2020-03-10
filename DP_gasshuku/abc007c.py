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
sy = sy - 1
sx = sx - 1
gy = gy - 1
gx = gx - 1

visited = [[False] * W for i in range(H)]
C = [list(input()) for i in range(H)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    que = deque([(sy, sx)])
    C[sy][sx] = 0
    visited[sy][sx] = True
    while que:
        y, x = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < W and 0 <= ny < H and C[ny][nx] != "#" and visited[ny][nx] == False:
                C[ny][nx] = C[y][x] + 1
                visited[ny][nx] = True
                que.append((ny, nx))
    print(C[gy][gx])

if __name__ == "__main__":
    bfs()
