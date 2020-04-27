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

A, B, C, X, Y = MAP()

ans = INF

ma = max(X, Y)
t = ma * C * 2
ans = A * X + B * Y
# print(ans, t)
# exit()
mi = min(X, Y)
mi_X = X - mi
mi_Y = Y - mi
tmp = mi_X * A + mi_Y * B + C * mi * 2
ans = min(ans, tmp, t)
print(ans)
exit()

# for i in range():
# print(ans)
for i in range(min(X, Y) + 1):
    tmp = A * (X - i) + B * (Y - i) + C * 2 * i
    print(tmp)
    ans = min(tmp, ans)
print(ans)




# i = 0
# new = 0
# while new < ans:
#     new = A * (X - i) + B * (Y - i) + C * 2 * i
#     ans = min(ans, new)
#     print(ans)
#     i += 1
# print(ans)
    # if new < ans:
    #     ans = new
    #     i += 1
    # else:
    #     print(ans)
    #     break