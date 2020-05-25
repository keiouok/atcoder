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

N, M = MAP()
L = [LIST() for i in range(M)]
graph = defaultdict(list)

q = deque([0])
for a, b in L:
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


# put = [0] * N
visited = [False] * N
goto = [INF] * N
dist = [INF] * N

dist[0] = 0
while q:
    a = q.popleft()
    visited[a] = True
    for node in graph[a]:
        if dist[node] > dist[a] + 1:
            dist[node] = dist[a] + 1
            # print("node, a", node, a, dist[node], dist[a])
            goto[node] = a
            q.append(node)

if False in visited:
    print("No")
else:
    print("Yes")
    for g in goto[1:]:
        print(g+1)

# print(dist)
# print(goto)
# print(visited)


