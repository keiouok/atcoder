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

T = INT()
ans = []
for i in range(T):
    L = LIST()
    L, R = L
    if L == 0 and R == 0:
        ans.append(1)
        continue
    r = R // 2
    a = R - L
    b = a - L + 1 # 3
    if b <= 0:
        ans.append(0)
        continue
    wa = b * (b + 1) // 2
    ans.append(wa)
print(*ans, sep="\n")