import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, floor
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

N, x = MAP()
A = LIST()

# Who are you?

# 最初のやつ
# マイナスにならないように
ans = max(0, A[0]-x)
# a[0] - xが負なら，0，正ならそのまま

# xの方が大きいなら，残りはなくなるので0
# xの方が小さいなら，残りがa[0] - x
a[0] = min(a[0], 0)

for i in range(1, N):
    a[i]
