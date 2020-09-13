import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
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

N = INT()
# L = [LIST() for i in range(N)]

zmax, zmin, wmax, wmin = -10 ** 9, 10 ** 9, -10 ** 9, 10 ** 9
# for i in range(N):
for i in range(N):
    x, y = MAP()
    zmax = max(zmax, x + y)
    zmin = min(zmin, x + y)
    wmax = max(wmax, x - y)
    wmin = min(wmin, x - y)
print(max(zmax - zmin, wmax - wmin))

