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

ans = INF

for i in range(2):
    if i == 1:
        H, W = W, H
    for a in range(1, H):
        bc = H - a
        b = int(bc/2)
        c = bc - b
        sa, sb, sc = a * W, b * W, c * W
        s = max(sa, sb, sc) - min(sa, sb, sc)
        ans = min(s, ans)
    for a in range(1, H):
        bc = H - a
        b = int(W/2)
        c = W - b
        sa, sb, sc = a * W, b * bc, c * bc
        s = max(sa, sb, sc) - min(sa, sb, sc)
        ans = min(s, ans)
print(ans)