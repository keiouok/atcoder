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
S = [input() for h in range(H)]
q = deque([(0, 0)])
# s : 0, 0
# g : H - 1, W - 1
visited = [[False] * W for i in range(H)]
dw = [0, 1, 0, -1]
dh = [1, 0, -1, 0]
dist = [[INF] * W for i in range(H)]
dist[0][0] = 1

dic = defaultdict(int)

for h in range(H):
    for w in range(W):
        dic[S[h][w]] += 1

if S[0][0] == "#":
    print("-1")
    exit()
while q:
    h, w = q.popleft()
    # if S[h][w] == "#":
    for i in range(4):
        nw = w + dw[i]
        nh = h + dh[i]
        if 0 <= nw < W and 0 <= nh < H:
            if S[nh][nw] != "#" and visited[nh][nw] == False:
                # dist[nh][nw] = min(dist[h][w] + 1, dist[nh][nw])
                dist[nh][nw] = dist[h][w] + 1
                visited[nh][nw] = True
                q.append((nh, nw))
# print(visited)
# print(*dist, sep="\n")
if dist[H-1][W-1] == INF:
    print(-1)
else:
    print(dic["."] - dist[H-1][W-1])
            

    



