import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

L, X, Y, S, D = MAP()

a, b = INF, INF
if D >= S:
    a = (D - S) / (X + Y)
    if Y > X:
        b = (L - D + S) / (Y - X)
else:
    if Y > X:
        a = (S - D) / (Y - X)
    b = (L - S + D) / (X + Y)
# print(a, b)
print(min(a, b))