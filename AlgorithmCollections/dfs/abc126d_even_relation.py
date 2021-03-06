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
L = [LIST() for i in range(N-1)]

graph = defaultdict(list)
for u, v, w in L:
    graph[u-1].append((v-1, w))
    graph[v-1].append((u-1, w))

color = [0] * N
color[0] = 1

def dfs(node):
    for i, w in graph[node]:
        if color[i] == 0: # not visited
            if w % 2 == 0: # guusuu        
                color[i] = color[node]
            else:
                color[i] = color[node] * (-1)
            dfs(i)

dfs(0)
for c in color:
    if c == 1:
        print(0)
    else:
        print(1)

        
