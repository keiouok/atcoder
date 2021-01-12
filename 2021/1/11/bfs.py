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

# 23:27 - 23:35
H, W = MAP()
sh, sw = MAP()
gh, gw = MAP()

sh, sw = sh - 1, sw - 1
gh, gw = gh - 1, gw - 1

A = [list(input()) for i in range(H)]
dist = [[INF] * W for i in range(H)]
visited = [[False] * W for i in range(H)]
dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

q = deque([(sh, sw)])
dist[sh][sw] = 0

ans = 0
while q:
    ch, cw = q.popleft()
    for i in range(4):
        nw = cw + dw[i]
        nh = ch + dh[i]
        if 0 <= nw < W and 0 <= nh < H:
            if dist[nh][nw] == INF and A[nh][nw] == ".":
                dist[nh][nw] = min(dist[ch][cw] + 1, dist[nh][nw])
                if nh == gh and nw == gw:
                    print(dist[nh][nw])
                    exit()
                q.append((nh, nw))

