import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left, bisect_right

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
A = LIST()
A.sort(reverse=True)
total = sum(A)
x, y = A[1], A[0]

B = []
for i in range(len(A)-1):
    B.append(A[i] - A[i + 1])
print(B)







exit()
# ans = abs(total)
cnt = 0
ans = 0
ans = abs(x - y)
# print(ans)
for i, a in enumerate(A):
    if i == 0 or i == 1:
        continue
    else:
        if a >= 0:
            if x <= y:
                nx = x + a
                ny = y
                # print(a)
            else:
                nx = x
                ny = y + a
                # print(a)
            # print("nx, ny:", nx, ny)
        else:
            if x > y:
                nx = x + a
                ny = y 
            else:
                nx = x
                ny = y + a
        # print(nx, ny, x, y)
        if abs(nx - ny) < abs(x - y):
            ans = abs(nx - ny)
            x = nx
            y = ny
        else:
            ans = abs(x - y)
            x = nx
            y = ny
print(ans)
            
    





#     cx = x
#     cy = y
#     nx = x + a
#     ny = y - a
#     if abs(nx - ny) < abs(x - y):
#         x = nx
#         y = ny
#         ans = abs(nx - ny)
#         cnt += 1
# if cnt == 0:
#     x = x + A[0]
#     y = y - A[0]
#     ans = abs(x - y)

# print(ans)




