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

N = INT()
a, b = MAP()
M = INT()
L = [LIST() for i in range(M)]

comb = [0] * N
graph = defaultdict(list)
dist = [INF] * N

for x, y in L:
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

q = deque([a-1])
visited = [False] * N
# startは0
dist[a-1] = 0
comb[a-1] = 1

def bfs():
    while q:
        n = q.popleft()
        d, c = dist[n], comb[n]
        for node in graph[n]:
            # d_next, c_next = dist[node], comb[node]
            if d + 1 < dist[node]:
                # 更新すべきd_nextの方が大きいなら，より小さいものに更新すべき
                dist[node] = d + 1
                # combはさっきと一緒，
                comb[node] = c
                if node not in q:
                    q.append(node)

            elif d + 1 == dist[node]:
                # コストが一緒のものと，分岐でちょうどマージ
                comb[node] = comb[node] + c
                # 同じなのでどっちでもいい
                # dist[node] = d + 1
                if node not in q:
                    q.append(node)
            else:
                continue
bfs()
print(comb[b-1]%mod)            
