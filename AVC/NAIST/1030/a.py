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

A, B, C = MAP()
# for a in range(A):
a = (A + 1) * A // 2
b = (B + 1) * B // 2
c = (C + 1) * C // 2
# c = 1 // 2 * (C + 1) * C
# ans =  (a + c) * (a + b) * (b + c)
ans = a * b * c
# print(ans)

# d = b * c
# ans = 0
# for a in range(1, A+1):
#     ans += a * (b * c)

print(ans % 998244353)