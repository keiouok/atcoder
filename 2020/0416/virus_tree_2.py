import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, K = MAP()
L = [LIST() for i in range(N-1)]
color = [0] * N
# color[]
graph = defaultdict(list)
for a, b in L:
    graph[a].append(b)
    graph[b].append(a)

ans = 1
# child, parent, kakerumono
q = deque([[1, 0, K]])
# color[0] = K
# visited = [False] * N
# visited[0] = True
while q:
    u, p, k_ = q.popleft()
    ans = (ans * k_) % mod
    if p == 0:
        # parentなし
        k_next = K - 1
    else:
        k_next = K - 2

    for v in graph[u]:
        if v == p:
            # 親と同じなら飛ばす
            continue
        q.append([v, u, k_next])
        # 子の数だけk_nextを減らしながら書けていく
        # K-2 P c_k
        k_next -= 1
print(ans)


