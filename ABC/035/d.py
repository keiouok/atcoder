import pdb
import heapq
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

def dijkstra(E, start):
    N_d = len(E)
    dist = [INF] * N_d
    dist[start] = 0
    q = [(0, start)]
    while q:
        dist_v, v = heapq.heappop(q)
    #    pdb.set_trace()
        if dist[v] != dist_v:
            continue
        for u, dist_vu in E[v]:
            dist_u = dist_v + dist_vu
            if dist_u < dist[u]:
                dist[u] = dist_u
                heapq.heappush(q, (dist_u, u))
    return dist

# E は 連結リスト(多分)
# startは始点

N, M, T = MAP()
A = LIST()
E = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = MAP()
    E[a-1].append((b-1, c))

# print(E)
# total = 0
d1 = dijkstra(E, 0)
# print(d1)
F = [[] for _ in range(N)]

for i, e in enumerate(E):
    # print(e)
    for t in e:
        # print(t)
        a = t[0]
        b = i
        c = t[1]
        F[a].append((b, c))


d2 = dijkstra(F, 0)
# print(d2)

total = []
for i in range(N):
    total.append(d1[i] + d2[i])
# print(total)

money = []
for i, t in enumerate(total):
    money.append((T - t) * A[i])
# print(money)
ans = max(money)
print(ans)
