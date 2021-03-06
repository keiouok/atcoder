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

R, G, B, N = MAP()


b_max = N // B
cnt = 0
for b in range(0, b_max+1):
    amari = N - B * b
    g_max = amari // G
    G * g_
    for g in range(0, g_max+1):
        sa = amari - G * g
        if sa >= 0:
            r = sa / R
            if r >= 0 and r == int(r):
                cnt += 1
print(cnt)
            

