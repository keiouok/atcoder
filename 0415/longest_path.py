import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from heapq import heapify, heappop, heappush

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, M = MAP()
gout = [[] for i in range(N)]
deg = [0] * N

for i in range(M):
    x, y = MAP()
    gout[x-1].append(y-1)
    deg[y-1] += 1
# only no_children 
topo = [v for v in range(N) if deg[v] == 0]
path_len = [0] * N
ans = 0
q = deque(topo)
# 子を持たない子スタート
while q:
    v = q.popleft()
    for t in gout[v]:
        # 親の子，vのカウントを減らす
        deg[t] -= 1
        # それでそれ以外の子がいなくなったら，
        # トポロジカルソートではスタックに積む
        if deg[t] == 0:
            q.append(t)
            path_len[t] = path_len[v] + 1
            ans = path_len[t]
print(ans)