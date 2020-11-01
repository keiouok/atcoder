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

ans = 0

for cd in range(2, 2 * N + 1):
    if cd - 1 <= N:
        p = cd - 1
    elif cd - N <= N:
        p = max(0, N - (cd - N) + 1)
    else:
        p = 0
        # print(cd)
    ab =  K + cd
    # -
    if ab - 1 <= N:
        q = max(ab - 1, 0)
    elif ab - N <= N:
        q = max(0, N - (ab - N) + 1)
    else:
        q = 0
        # print(ab)
    ans += p * q
print(ans)
