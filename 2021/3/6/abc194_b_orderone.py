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
L = [LIST() for i in range(N)]

A = []
B = []

for i in range(N):
    A.append(L[i][0])
    B.append(L[i][1])

i = A.index(min(A))
j = B.index(min(B))

if i == j:
    a, b = A[i], B[i]
    del A[i]
    del B[i]
    # print(A, B)
    ans = min(a + b, max(min(A), b), max(a, min(B)))
else:
    ans = max(A[i], B[j])
print(ans)