import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import groupby, accumulate, permutations, combinations, product
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

A = [k for k, g in groupby(A)]
N = len(A)
i = 1
ans = 0
while i < N - 1:
    if A[i-1] < A[i] > A[i+1] or A[i-1] > A[i] < A[i+1]:
        ans += 1
        # 1つ右は見なくていいので飛ばせる
        i += 1
    i += 1
print(ans+1)