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

N, M = MAP()
L = [LIST() for i in range(M)]

dic = defaultdict(list)

## UnionFind(強い方を新調)

class UnionFind():
    def __init__(self, n):
        self.n = n
        # parents[i]: 要素iの親要素の番号
        # 要素iが根の場合、parents[i] = -(そのグループの要素数)
        self.parents = [-1] * n
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    # 要素xが属するグループの要素数を返す
    def size(self, x):
        return -self.parents[self.find(x)]
    def same(self, x, y):
        return self.find(x) == self.find(y)
    # 要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    # 全ての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    # グループの数を返す
    def group_count(self):
        return len(self.roots())
    # 辞書{根の要素: [****そのグループに含まれる要素のリスト****], ...}を返す
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    # print()での表示用
    # all_group_members()****をprintする****
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

tree = UnionFind(N)

for a, b in L:
    dic[a-1].append(b-1)
    dic[b-1].append(a-1)

q = deque([0])

visited = [False] * N
dist = [INF] * N
dist[0] = 0
cnt = [0] * N
cnt[0] = 1

while q:
    a = q.popleft()
    na_list = dic[a]
    for na in na_list:
        # if visited[na] == True:
        #     continue
        if dist[na] > dist[a] + 1:
            dist[na] = dist[a] + 1
            # path[na] += path[a]
            cnt[na] = cnt[a]
            q.append(na)
        elif dist[na] == dist[a] + 1:
            cnt[na] += cnt[a]

print(cnt[-1] % mod)

# print(dist)

# q = deque([0])
# ans = 1

# # dicdist = defaultdict(list)

# parent = [0] * N
# while q:
#     a = q.popleft()
#     # na_des = a + 1
#     cnt = 0
#     print(dic[a])
#     for na in dic[a]:
#         if dist[na] == dist[a] + 1:
#             # cnt += 1
#             parent[a] = parent[a] * parent[na] + 1
#             q.append(na)
#     # if cnt != 0:
#     # ans *= cnt
# print(parent)
# print(ans)
