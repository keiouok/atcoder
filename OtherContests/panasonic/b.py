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

H, W = MAP()
if H == 1 or W == 1:
    print(1)
    exit()
if H % 2 == 0 and W % 2 == 0:
    a = H * W // 2
if H % 2 == 0 and W % 2 != 0:
    a = H * W // 2
if H % 2 != 0 and W % 2 == 0:
    a = (H - 1) * W // 2 + (W // 2)
if H % 2 != 0 and W % 2 != 0:
    a = (H - 1) * W // 2 + (W // 2 + 1)
print(a)

# exit()
# if H == 1 or W == 1:
#     print(1)
#     exit()

# if H % 2 == 0:
#     print(H * W // 2)
# else:
#     a = (H - 1) // 2 * W + (W - 1)
#     print(a)





# exit()
# if W % 2 == 0:
#     a = W // 2
#     b = W // 2
# else:
#     a = W // 2 + 1
#     b = W // 2
# # a = ceil(W / 2)
# # b = ceil((W-1) / 2)
# print(a)
# print(b)
# if H % 2 == 0:
#     ans = a * H // 2 + b * H // 2
#     print(H//2)
#     print(H//2)
# else:
#     ans = a * (H // 2+1) + b * H // 2
#     print(H//2+1)
#     print(H//2)
# print(ans)