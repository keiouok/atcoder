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
dist = [INF] * N
for a, b, c in L:
    E[a-1].append((b-1, c))
