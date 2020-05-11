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

N, K = MAP()
A = LIST()

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

graph = defaultdict(list)
g = defaultdict(list)
E = [[] for i in range(N)]
visited = [False] * N
for i, a in enumerate(A):
    graph[i].append((a-1, 1))
    g[i].append(a-1)
q = deque([0])
# ma = 0
order = []
while q:
    a = q.popleft()
    if visited[a] == True:
        last_idx = a
        break
    visited[a] = True
    order.append(a)

    for node in g[a]:
        q.append(node)

for i, a in enumerate(order):
    if a == last_idx:
        order_idx = i
# print(order_idx)
if K < order_idx:
    print(order[K]+1)
else:
    order_syuki = order[order_idx:]
    len_syuki = len(order_syuki)
    saigo_num = K - order_idx
    i_in_here = saigo_num % len_syuki
    ans = order_syuki[i_in_here]
    print(ans+1)


# if K <= 

# ma_d = ma - d[last_idx]
# mi_d = d[last_idx]
# print(ma_d, mi_d)



