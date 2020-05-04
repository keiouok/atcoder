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

N = INT()
S = list(input())
c = Counter(S)
w = c["W"]
e = c["E"]
al = w + e
# WWWWW -> EEEEE
# 変えるべきE
ans = e
num_w, num_e = 0, e
for i in range(N):
    sign = S[i]
    if sign == "W":
        w += 1
        al = al + 1
        num_w += 1
    elif sign == "E":
        num_e -= 1
    ans = min(ans, num_e + num_w)
print(ans)

