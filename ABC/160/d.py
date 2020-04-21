import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from heapq import heappop, heappush, heapify

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

N, X, Y = MAP()

# graph = defaultdict(list)
dp = [[INF] * N for i in range(N)]

for i in range(N):
    dp[0][i] = i
# dp[0][0] = 0
for i in range(N):
    dp[i][0] = i

dp[0][Y-1] = X + 1
dp[Y-1][0] = X + 1

for i in range(1, N):
    for j in range(i, N):
        dp[i][j] = min(dp[i][j-1] + 1, dp[i][j])
        # dp[i][N-j] = min(dp[i][N-j], dp[i][N-j])
for i in range(N-1, 0 -1):
    for j in range(i, 0, -1):
        dp[i][j-1] = min(dp[i][j] + 1, dp[i][j-1])
print(dp)
exit()
    
#     for j in range(N):
#         dp[i][j] += 

# dp[0][0] = 0
# for i in range(N-1):
#     for j in range(N-1):

# exit()
for i in range(N-1):
    graph[i].append((i+1, 1))
    graph[i+1].append((i, 1))

graph[X-1].append((Y-1, 1))
graph[Y-1].append((X-1, 1))

# a = dijkstra(graph, 0)
count = defaultdict(int)
for i in range(N):
    a = dijkstra(graph, i)
    # print(a)
    # print(a[i+1:])
    for c in a[i+1:]:
        count[c] += 1
# print(count)

for i in range(1, N):
    print(count[i])