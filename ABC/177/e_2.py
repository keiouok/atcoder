import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
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

if reduce(gcd, A) != 1:
    print("not coprime")
    exit()
ma = max(A)
p = list(range(ma+1))

for x in range(2, int(ma ** 0.5) + 1):
    if p[x]:
        # xは素数，それがpの要素にあるうちは続ける
        for i in range(2 * x, ma + 1, x):
            p[i] = x

s = [set() for _ in range(N)]
t = set()

for i, x in enumerate(A):
    while x != 1:
        s[i].add(x)
        t.add(x)
        # 割り続けるとs[i]にその素数がたまっていく
        x //= p[x]
l = sum(len(x) for x in s)
print("pairwise coprime" if l == len(t) else "setwise coprime")
