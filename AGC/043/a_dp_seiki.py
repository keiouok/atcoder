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

cost = [[INF] * (W + 1) for i in range(H + 1)]

field = ["#" * (W + 1)]

for i in range(H):
    line = input()
    field.append("#" + line)

if field[1][1] == "#":
    cost[1][1] = 1
else:
    cost[1][1] = 0

for i in range(1, H + 1):
    for j in range(1, W + 1):
        if i * j == 1:
            continue
        # そのまま
        if field[i][j] == ".":
            cost[i][j] = min(cost[i-1][j], cost[i][j-1])
        else:# 今いるところが黒
            up_cost = cost[i-1][j]
            left_cost = cost[i][j-1]
            # 上が黒
            if field[i-1][j] == ".":
                up_cost += 1
            if field[i][j-1] == ".":
                left_cost += 1
            
            cost[i][j] = min(up_cost, left_cost)
print(cost[H][W])
