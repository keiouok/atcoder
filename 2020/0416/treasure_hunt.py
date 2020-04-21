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

def dijkstra(E, start):
    N_d = len(E)
    dist = [INF] * N_d
    dist[start] = 0
    q = [(0, start)]
    while q:
        dist_v, v = heappop(q)
        if dist[v] != dist_v:
            continue
        for u, dist_vu in E[v]:
            dist_u = dist_v + dist_vu
            if dist_u < dist[u]:
                dist[u] = dist_u
                heappush(q, (dist_u, u))
    return dist

N, M, T = MAP()
A = LIST()
L = [LIST() for i in range(M)]

# graph = [[] for i in range(N)]
graph = defaultdict(list)
for a, b, c in L:
    graph[a-1].append((b-1, c))

dist1 = dijkstra(graph, 0)

F = defaultdict(list)

# print(graph)
for a, b, c in L:
    F[b-1].append((a-1, c))

dist2 = dijkstra(F, 0)

# これダメ
# for i in range(N):
#     dist2[i] = dijkstra(graph, i)[0]

goback_time = [(T-(dist1[i]+dist2[i])) * A[i] for i in range(N)]
# dist = [T - d * 2 for d in dist]
# print(dist)
# print(goback_time)
ans = 0

# for i, d in enumerate(goback_time):
#     ans = max(ans, d * A[i])
# print(ans)
print(max(goback_time))
