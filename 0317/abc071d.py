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
s1 = input()
s2 = input()

r = 0
ans = 1

pre_is_x = True
while r < N:
    if r == 0:
        if s1[r] == s2[r]:
            # x
            ans *= 3
            r += 1
            pre_is_x = True
        else:
            # y
            ans *= 6
            r += 2
            pre_is_x = False
    # if pre_is_x == True:

    elif s1[r] == s2[r]:
        # x
        if pre_is_x == True:
            # from x
            ans *= 2
        else:
            # from y
            ans *= 1
        r += 1
        pre_is_x = True
    else:
        # y
        if pre_is_x == True:
            # from x
            ans *= 2
        else:
            # from y
            ans *= 3
        r += 2
        pre_is_x = False

print(ans % mod)



    # ここからが左以外


# exit()
# while r > N:
#     if s1[r] == s2[r]:
#         # ans *= 1
#         if r == 0:
#             ans *= 1
#         # r-1
#         # r += 1
#         if s1[r-1] == s2[r-1]:
#             ans *= 2
#         if s1[r-1] == s2[r-1]:
#             ans *= 1
#         r += 1

#     else:
#         s1[r] != s2[r]:
#         ans *= 2
#         r += 2
        