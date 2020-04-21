import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
import numpy as np

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))

sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7


N, Q = MAP()
A = []
P = []
# G = np.eye(N+1)
# G = np.zeros(N+1)
# print(G)
l_G = [[0]*(N+1) for i in range(N+1)]
# print(np.array(G))
G = np.array(l_G)


for i in range(N-1):
    A.append(LIST())
for i in range(Q):
    P.append(LIST())
print(A)
print(P)
ans = [0] * (N+1)
for p in P:
    for a in A:
        print(a)
        # sonomono
        if p[0] == a[0]:
            ans[a[1]] += p[1]
            print(ans)
    ans[p[0]] += p[1]
print(ans)


for a in A:
    x = a[0]        
    y = a[1]
    print("x,y")
    print(x, y)
    G[x][y] += 1
    G[y][x] += 1
#         G[]
print(G)

# for p in P:
#     G[0][p[0]] += p[1]
#     G[p[0]][0] += p[1]
    
# print(G)

s = []
for i in range(len(G)):
    for j in range(len(G)):
        if G[i][j] == 1:
            s.append(j)
        print(s)
    




        # if a[0]
        # if P[i][0] == a[0]:
        #     ans[a[1]] += P[i][1]
    

        
        