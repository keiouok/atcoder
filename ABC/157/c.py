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

N, M = MAP()
L = [LIST() for i in range(M)]

kaburi = []
num = [-1] * N
# saisyo ga 0
# if N > 1:
#     for l in L:
#         s, c = l
#         if s == 1 and c == 0:
#             print(-1)
#             exit()

for l in L:
    s, c = l
    if num[s-1] == -1:
        num[s-1] = c
    elif num[s-1] == c:
        num[s-1] = c
    else:
        print("-1")
        exit()

    # if s in kaburi and :
        # print(-1)
        # exit()
    # kaburi.append(s)
    # print(kaburi)
    # num[s-1] = c
#
if N != 1 and num[0] == 0:
    print(-1)
    exit()

if N == 1 and num[0] < 1:
    print(0)
    exit()
# print(num)
ans = []

for i in range(N):
    if i == 0:
        if num[i] == -1:
            ans.append("1")
        else:
            ans.append(str(num[i]))
    else:
        if num[i] != -1:
            ans.append(str(num[i]))
        else:
            ans.append("0")


# if N != 1 and ans[0] == "0":
#     print(-1)
#     exit()
print("".join(ans))
