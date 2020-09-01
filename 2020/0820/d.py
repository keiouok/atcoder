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
C = LIST()
D = LIST()
S = [input() for i in range(H)]

visited = [[False] * W for i in range(H)]
dist = [[INF] * W for i in range(H)]
q = deque([(C[0]-1, C[1]-1)])

dist[C[0]-1][C[1]-1] = 0
visited[C[0]-1][C[1]-1] = True
dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]
warp = [[-1] * W for i in range(H)]
warp[C[0]-1][C[1]-1] = 0
warp_time = 0
warp_stock = deque([[C[0]-1, C[1]-1]])

while q or warp_stock:
    while q:
        ch, cw = q.popleft()
        warp_stock.append([ch, cw])
        dh = [0, 1, 0, -1]
        dw = [1, 0, -1, 0]
        for i in range(4):
            nh = ch + dh[i]
            nw = cw + dw[i]
            if 0 <= nh < H and 0 <= nw < W:
                if visited[nh][nw] == False and S[nh][nw] != "#":
                    # dist[nh][nw] = dist[ch][cw] + 1
                    visited[nh][nw] = True
                    warp[nh][nw] = warp_time
                    # warp_stock.append([nh, nw])
                    q.append([nh, nw])
        # print(warp_stock)
    while warp_stock:
        ch, cw = warp_stock.popleft()
        for dh in [-2, -1, 0, 1, 2]:
            for dw in [-2, -1, 0, 1, 2]:
                nh = ch + dh
                nw = cw + dw
                if 0 <= nh < H and 0 <= nw < W:
                    if visited[nh][nw] == False and S[nh][nw] != "#":
                        # dist[nh][nw] = dist[ch][cw]
                        visited[nh][nw] = True
                        q.append([nh, nw])
                        warp[nh][nw] = warp_time + 1
    warp_time += 1
print(warp[D[0]-1][D[1]-1]) 
# print(warp)

    