import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from heapq import heappop, heappush, heapify
import heapq

 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

X, Y, A, B, C = MAP()
P = LIST()
Q = LIST()
R = LIST()

p = []
q = []
r = []

for a in P:
    p.append((-1) * a)

for b in Q:
    q.append((-1) * b)

for c in R:
    r.append((-1) * c)

heapify(p)
heapify(q)
heapify(r)

a = []
b = []
c = []
ans = 0
for i in range(X):
    x = (heappop(p)) * (-1)
    y = (heappop(r)) * (-1)
    if x >= y:
        ans += x
        heappush(r, -1 * y)
    else:
        ans += y
        heappush(p, -1 * x)

for j in range(Y):
    x = (heappop(q)) * (-1)
    y = (heappop(r)) * (-1)
    if x >= y:
        ans += x
        heappush(r, -1 * y)
    else:
        ans += y
        heappush(q, -1 * x)

# for k in range(X + Y):
#     x = heappop()
#     c.append(x)
print(ans)
# dp = [INF] * 
# print(max(P) + max(Q) + max(R))


