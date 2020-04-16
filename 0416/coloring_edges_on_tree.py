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
edge = defaultdict(int)

for a, b in L:
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

K = 0
# 子の数が最大となるものの子の数が，塗れる色の最大値
for v in graph.values():
    K = max(K, len(v))

# this is color pallet
color = list(range(1, K + 1))
# color = [1, ..., K]
q = deque()
q.append((0, None))
while q:
    i, color_from = q.popleft()
    tmp = -1
    # colorの後ろから見れるように
    for node in graph[i]:
        str_ = "{},{}".format(i, node)
        # まだedge辞書になければ
        if not edge[str_]:
            use_color = color[tmp]
            if use_color == color_from:
                # さらに小さい色のやつ
                tmp -= 1
                use_color = color[tmp]
            # 次対策
            tmp -= 1
            edge[str_] = use_color
            edge["{},{}".format(node, i)] = use_color
            q.append((node, use_color))
print(K)
for a, b in L:
    print(edge["{},{}".format(a-1, b-1)])

