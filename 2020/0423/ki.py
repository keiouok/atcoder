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

N, Q = MAP()
A = [LIST() for i in range(N-1)]
P = [LIST() for i in range(Q)]

graph = defaultdict(list)
for a, b in A:
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

cnt = [0] * N
ans = [0] * N

for node, point in P:
    cnt[node-1] += point

check = [False] * N
q = deque([])
q.append(0)
check[0] = True

while q:
    a = q.pop()
    for node in graph[a]:
        if check[node] == True:
            continue
        cnt[node] += cnt[a]
        check[node] = True
        q.append(node)
print(*cnt)



