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

# 19:22 - 
H, W = MAP()
A = [list(input()) for i in range(H)]


# 黒探索
q = deque([])
for h in range(H):
    for w in range(W):
        if A[h][w] == "#":
            q.append((h, w))
visited = [[False] * W for i in range(H)]
dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]
dist = [[0] * W for i in range(H)]

ans = 0
while q:
    ch, cw = q.popleft()
    # visited[ch][cw] = True
    for i in range(4):
        nw = cw + dw[i]
        nh = ch + dh[i]
        if 0 <= nw < W and 0 <= nh < H:
            if visited[nh][nw] == False and A[nh][nw] == ".":
                dist[nh][nw] = dist[ch][cw] + 1
                ans = max(ans, dist[nh][nw])
                visited[nh][nw] = True
                q.append((nh, nw))

# print(dist)
print(ans)
                


