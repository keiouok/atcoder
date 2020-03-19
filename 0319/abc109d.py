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

H, W = MAP()
A = [LIST() for i in range(H)]

xy = []
xxyy = []
route = []
sum_A = 0

for i in range(H):
    if i % 2 == 0:
        for j in range(W):
            route.append([i, j])
    else:
        for j in range(W-1, -1, -1):
            route.append([i, j])
    sum_A += A[i][j]
# print(route)
ans = []
for i in range(len(route)-1):
    y, x = route[i]
    y_next, x_next = route[i+1]
    if A[y][x] % 2 == 1:
        A[y][x] -= 1
        A[y_next][x_next] += 1
        ans.append([y+1, x+1, y_next+1, x_next+1])
print(len(ans))
for a in ans:
    print(*a)




