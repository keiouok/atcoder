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

graph = defaultdict(list)
rinsetsu = [[0] * N for i in range(N)]

for a, b in L:
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    rinsetsu[a-1][b-1] = 1
    rinsetsu[b-1][a-1] = 1

per = list(permutations([n for n in range(1, N)]))
permu = []
for p in per:
    p = [0] + list(p)
    permu.append(p)
ans = 0
for p in permu:
    cnt = 0
    for i in range(N-1):
        a, b = p[i], p[i+1]
        if rinsetsu[a][b] == 1:
            cnt += 1
    if cnt == N - 1:
        ans += 1
print(ans)
        

