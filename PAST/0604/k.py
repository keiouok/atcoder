import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, bisect_right
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

N, Q = MAP()
L = [LIST() for i in range(Q)]

table = [[i] for i in range(N+1)]

for f, t, x in L:
    l = table[f]
    # idx = bisect_left(l, x)
    # print(l, x, idx)
    stack = l[idx:]
    table[t] += stack
    table[f] = l[:idx]
print(table)
