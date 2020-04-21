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

A, B = MAP()
C = []

for i in range(50):
    C.append(["#"] * 100)
for i in range(50):
    C.append(["."] * 100)

h = 0
w = 0
for i in range(A-1):
    C[h][w] = "."
    w += 2
    if w >= 100:
        # 端まで行ったら最初っから
        w = 0
        # 一行開けて下に書く
        h += 2

# 下から．二次元でもできる．
h = -1
w = 0

for i in range(B-1):
    C[h][w] = "#"
    w += 2
    if w >= 100:
        # 端まで行ったら最初っから
        w = 0
        # 一行開けて下に書く
        h -= 2

print(100, 100)
for i in range(100):
    print(*C[i], sep="")