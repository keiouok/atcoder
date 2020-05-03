import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
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

N, M, Q = MAP()
L = [LIST() for i in range(Q)]

ans = 0
A_list = list(combinations_with_replacement(range(1, M+1), N))
for A in A_list:
    tmp = 0
    for a, b, c, d in L:
        if A[b-1] - A[a-1] == c:
            tmp += d
    ans = max(tmp,ans)
print(ans)

