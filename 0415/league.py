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

N = INT()
A = [LIST() for i in range(N)]

match_id = [[0] * N  for i in range(N)]


cnt = 0
for i in range(N):
    for j in range(N):
        if i < j:
            match_id[i][j] = cnt
            cnt += 1

def toid(i, j):
    if i > j:
        i, j = j, i
    return match_id[i][j]

V = N * (N - 1) // 2
gout = [[] for _ in range(V)]
deg = [0] * V
for i in range(N):
    for j in range(N - 2):
        gout[toid(i, A[i][j]-1)].append(toid(i, A[i][j+1]-1))
        deg[toid(i, A[i][j+1]-1)] += 1

topo = [v for v in range(V) if deg[v] == 0]
day = [0] * V
q = deque(topo)
ans = 0
while q:
    v = q.popleft()
    for t in gout[v]:
        deg[t] -= 1
        if deg[t] == 0:
            q.append(t)
            day[t] = day[v] + 1
            ans = day[t]
if any(deg):
    # まだ1とかがある
    print(-1)
    exit()
print(ans + 1)








