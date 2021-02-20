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

N, K = MAP()

l = list(str(N))

small = int("".join(sorted(l)))
large = int("".join(sorted(l, reverse=True)))
# print(a, b)

# a = N
a = N
# print(l)
for i in range(K):
    l = list(str(a))
    small = int("".join(sorted(l)))
    large = int("".join(sorted(l, reverse=True)))
    # print(large - small)
    # print(small, large)
    a = large - small
print(a)

