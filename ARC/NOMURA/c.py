import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
import math
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

N = INT()
A = LIST()

ans = 0

b = A[N]

# v = 2 ** (N-1)
for i in range(N, 0, -1):
    # if N - 1 == i:
    #     ans += A[N-1]
    # else:
    d = 2 ** (i-1)
    # print("d", d)
    # print("b", b)
    ans += b
    # print("ans", ans)
    # print(b)
    # c = ceil(math.log2(b))
    c = ceil(b / 2)
    if A[i-1] + c <= d:
        b = A[i-1] + c
    else:
        print(-1)
        exit()

print(ans+b)
