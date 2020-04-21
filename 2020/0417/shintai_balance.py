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
S, T = MAP()
L = [LIST() for i in range(M)]

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

E = [[] for i in range(N)]
for a, b, c in L:
    E[a-1].append((b-1, c))
    E[b-1].append((a-1, c))

dist1 = dijkstra(E, S-1)
dist2 = dijkstra(E, T-1)
d = [(dist1[i], i + 1) for i in range(N) if dist1[i] == dist2[i] and dist1[i] != INF]
# print(d)
# print(dist1, dist2)
if not d:
    print(-1)
else:
    d.sort()
    print(d[0][1])