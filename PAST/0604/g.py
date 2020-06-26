import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, X, Y = MAP()
L = [LIST() for i in range(N)]
cannnot = [[False] * (X + 1) for i in range(Y + 1)]
for x, y in L:
    cannnot[y][x] = True

gx, gy = X, Y

visited = [[False] * (X + 1) for y in range(Y + 1)]
dist = [[INF] * (X + 1) for y in range(Y + 1)]
# print(dist)
C = []
q = deque([(0, 0)])
dist[0][0] = 0
visited[0][0] = True


dx = [1, 0, -1, 1, -1, 0]
dy = [1, 1, 1, 0, 0, -1]

while q:
    sy, sx = q.popleft()
    # if 0 <= next_x <  and 0 <= next_y
    for i in range(6):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if 0 <= nx < X + 1 and 0 <= ny < Y + 1 and visited[ny][nx] == False and cannnot[ny][nx] == False:
            dist[ny][nx] = min(dist[sy][sx] + 1, dist[ny][nx])
            visited[ny][nx] = True
            q.append((ny, nx))
# print(dist)
print(dist[gy][gx])
        


    