# なぜかうまくいかない
import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_right, bisect_left

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

A, B, Q = MAP()
S = [INT() for i in range(A)]
T = [INT() for i in range(B)]
X = [INT() for i in range(Q)]
S.insert(0, -INF)
S.append(INF)
T.insert(0, -INF)
T.append(INF)

for x in X:
    s = bisect(S, x)
    t = bisect(T, x)
    # print(s, t)
    # a = min(x - S[s-1], S[s] - x)
    # b = min(x - T[t-1], T[t] - x)
    res = INF
    for a in [S[s-1], S[s]]:
        for b in [T[t-1], T[t]]:
            res = min(res, min(abs(a - x) + abs(b - a), abs(x - b) + abs(b - a)))
    print(res)    
    

