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
    # 辞書{根の要素: [そのグループに含まれる要素のリスト], ...}を返す
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    # print()での表示用
    # all_group_members()をprintする
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

N, M = MAP()
L = [LIST() for i in range(M)]

graph = defaultdict(list)
tree = UnionFind(N)
for u, v in L:
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
    tree.union(u-1, v-1)

s_list = tree.roots()
visited = [False] * N

def dfs(from_n, to_n):
    s = [(from_n, to_n)]
    is_tree = True
    while s:
        from_n, to_n = s.pop()
        # visited.append(a)
        # print("graph of :", a , graph[a])
        for node in graph[to_n]:
            if node == from_n:
                pass
            elif visited[node] == True:
                is_tree = False
            else:
                visited[node] = True
                s.append((to_n, node))
    return is_tree
    
ans = 0

print(sum([dfs(r, r) for r in s_list]))

# for r in s_list:
#     ans += dfs(r, r)
# print(ans)

    #     for node in graph[a]:
    #         print("visited:", visited)
    #         print("graph[a]", graph[a])
    #         if node != a:
    #             if visited[node] == False:
    #                 # not yet visited
    #                 visited[node] = True
    #                 s.append(node)
    #             else:
    #                 is_tree = False
                    
    #                 print("HEREEEEEEEEEEEEEEEEE")
    #                 print("a, node", a, node)
    #                 print("s", s)
    #                 # visited.append(node)
    # print(visited)
    # print(is_tree)
    # print(s)
    # return is_tree






