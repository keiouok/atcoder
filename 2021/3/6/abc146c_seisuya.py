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

A, B, X = MAP()

def solve(N):
    return A * N + B * len(str(N))

ok = 0
ng = pow(10, 18) + 1

# 全部買える場合
if solve(10 ** 9) <= X:
    print(10 ** 9)
# 壱個も変えない
# elif solve(1) > X:
#     print(0)

else:
    while (ng - ok) > 1:
        mid = (ng + ok) // 2
        if solve(mid) <= X:
            ok = mid
        else:
            ng = mid

    # print(ok, ng, mid)
    print(ok)