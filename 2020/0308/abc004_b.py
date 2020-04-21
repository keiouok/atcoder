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

c = [input() for i in range(4)]

ans = [[0] * 4 for i in range(4)]
for i in range(4):
    c[i] = c[i][::-1]

for i in range(4):
    print(*c[4-1-i], sep=" ")

#     for w in range(4):
#         ans[4-h-1][4-w-1] = L[h][w]
# print(*ans, sep="\n")
