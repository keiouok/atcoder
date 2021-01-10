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

N = INT()
A = LIST()
a = 2 ** N // 2

l = A[:a]
r = A[a:]
# print(l, r)
l_ma = max(l)
r_ma = max(r)
# L = []
l_i = 0
r_i = 0
for i, a in enumerate(l):
    if a == l_ma:
        l_i = i + 1
        break
        
for i, b in enumerate(r):
    if b == r_ma:
        r_i = i + 1 + 2 ** N // 2
        break

# ans = min(max(l), max(r))
if l_ma < r_ma:
    print(l_i)
else:
    print(r_i)

