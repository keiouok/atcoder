import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
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

sx, sy = MAP()
gx, gy = MAP()

dx = gx - sx
dy = gy - sy

# 1で飛べるとき
# print(dx, dy)

if dx == 0 and dy == 0:
    ans = 0
elif abs(dx) + abs(dy) <= 3:
    ans = 1
# 斜めで一回で行ける
elif abs(dx / dy) == 1:
    ans = 1

elif dx % 2 == dy % 2:
    ans = 2
else:
    # 一回飛んでから以内にあればOK
    # ans = min(abs(dx - dy) + 1, 3)
    if abs(abs(dx) - abs(dy)) <= 3:
        ans = 2
    else:
        ans = 3 
print(ans)



# exit()
# # print(dx, dy)

# mi = min(dx, dy)
# ma = max(dx, dy)
# import math
# sa = ma - mi
# # 斜めなし
# # dx, dy

# ans0 = math.ceil(dx / 3) + math.ceil(dy / 3)

# # 1
# ans1 = 1 + math.ceil(sa / 3)

# # 斜め斜め残り
# y = 1 / 2 * (sy - sx + gy + gx)
# x = - 1 / 2 * (sy - sx + gy + gx) + gy + gx
# # print(x, y)
# a, b = int(x), int(y)

# c = gx - a
# d = -(gy - b)

# left = math.ceil(abs(c) / 3) + math.ceil(abs(d) / 3)
# ans4 = 1 + left

# # print(c, d)
# last_s = abs(c - d)
# if last_s == 0:
#     ans2 = 2
# else:
#     ans2 = 3
# # print(last_s)

# # ans2 = 1 + 1 + math.ceil(last_s/3)
# # print(ans0, ans1, ans2, ans4)
# print(min(ans0, ans1, ans2, ans4))
