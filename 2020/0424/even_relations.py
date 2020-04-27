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
L = [LIST() for i in range(N-1)]
graph = defaultdict(list)

for u, v, w in L:
    graph[u-1].append((v-1, w))
    graph[v-1].append((u-1, w))

color = [0] * N
visited = [False] * N

q = deque([0])
visited[0] = True
color[0] = 1

while q:
    a = q.pop()
    for node, w in graph[a]:
        if visited[node] == True:
            continue
        if w % 2 == 0:
            color[node] = color[a]
        else:
            color[node] = -1 * color[a]
        visited[node] = True
        q.append(node)
print(*[0 if c == 1 else 1 for c in color])

