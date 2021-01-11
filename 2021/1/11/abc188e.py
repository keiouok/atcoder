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

# 12:28
N, M = MAP()

A = LIST()
L = [LIST() for i in range(M)]

graph = [[] for _ in range(N)]

for x, y in L:
    # edge
    graph[x-1].append(y-1)
        
ans = -INF
dp = [-INF] * N
for v in range(N - 1, -1, -1):
    # 降順
    for nv in graph[v]:
        dp[v] = max(dp[v], dp[nv], A[nv])
    ans = max(ans, dp[v] - A[v])
print(ans)    


# print(dp)


# for i in range(N):
#     q = deque([i])
#     visited = [False] * N
#     dp = [INF] * N
#     while q:
#         j = q.popleft()
#         next_j_s = graph[j]
#         for next_j in next_j_s:
#             dp[next_j] = min(dp[next_j], dp[j], A[j])
#             q.append(next_j)
#             visited[j] = True
#     print(dp)
#     for i, v in enumerate(visited):
#         if v == True:
#             ans = max(A[i] - dp[i], ans)
# print(ans)


        





