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

N, M = MAP()
uv = [LIST() for i in range(M)]

graph = defaultdict(list)

# グラフの連結情報を登録
for u, v in uv:
    # つながり，無向グラフなので，両方
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
# そのノードは訪問済みかどうか
visited = [False] * N
# under
# flag = True  閉じてない
# flag = False 閉じてる
def dfs(from_n, to_n):
    global flag
    for node in graph[to_n]:
        if node == from_n:
            # 自分のnodeに帰る
            # 重要じゃないので無視しよう
            pass
        elif visited[node] == True:
            # すでに訪問してる：閉路
            flag = False
        else:
            # 訪問したマークつける
            visited[node] = True
            # 
            dfs(to_n, node)
    return flag

ans = 0
for i in range(N):
    if visited[i] == True:
        continue
    visited[i] = True
    flag = True
    if dfs(i, i):
        ans += 1
print(ans)


