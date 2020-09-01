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

x, k, d = MAP()

# if x >= 0 and x - k * d <= 0:


# a = x
# b = abs(x - k * d)
# c = b % d
# print(c,b)

# a = x % k
# b = x % d
if x > 0:
    if x - (k * d) < 0:
        b = abs(x - (k * d)) % d
        a = d - b
        # p = x % d
        # print(r, p)
        # print(min(a, b))
        # print(x % abs(x - (k * d)))
        f = x % abs(x - (k * d))
        # g = abs()
        # g = abs(d - f)
        # print(min(f, g))
        # print(f)
        print(abs(x - (k * d)) % d)
        # 1000000000000000 1000000000000000 1000000000000000
        print(d - (abs(x - (k * d)) % d))
        # print(1)
    else:
        print(x - (k * d))
        print(2)
else:
    if x + (k * d) > 0:
        b = (x + (k * d)) % d
        a = d - b
        # p = abs(x) % d
        # print(min(r, p))
        # print(abs(x) % abs(x + k * d))
        print(min(a, b))
        print(3)
    else:
        print(x + k * d)
        print(4)
