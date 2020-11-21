import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
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

N, M = MAP()

L = [LIST() for i in range(M)]

graph = defaultdict(list)

for u, v, c in L:
    graph[u-1].append([v-1, c-1])
    graph[v-1].append([u-1, c-1])

q = deque([0])

ans = [-1] * N
ans[0] = 0
while q:
    cv = q.popleft()
    for nv, c in graph[cv]:
        if ans[nv] != -1:
            # 行ったことある
            continue
        if ans[cv] == c:
            ans[nv] = (c + 1) % N
        else:
            ans[nv] = c
        q.append(nv)

for i in range(N):
    print(ans[i] + 1)

# k**9 