import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left
 
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
X, Y = MAP()
A = LIST()
B = LIST()

# nibutan ver.
time = 0
ans = 0
while 1:
    # timeが入るidxは，配列のidx目の左
    idx = bisect_left(A, time)
    # 超えてる
    if idx == len(A):
        break
    time = A[idx]
    time += X
    idx = bisect_left(B, time)
    if idx == len(B):
        break
    time = B[idx]
    time += Y
    ans += 1
print(ans)

