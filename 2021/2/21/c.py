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

tmp = 0
for a in A:
    tmp += a**2

sum = A[-1]
tmp2 = 0
for i in range(N-1):
    # print(A[N-i-1-1], sum)
    y = A[N-i-1-1]
    tmp2 += sum * y
    sum += y

ans = (N-1) * tmp + (-2) * tmp2


print(ans)
# tmp2 = 0
# for i in range(N-1):
#     tmp2 += A[i] * A[i+1]
# tmp2 += A[0] * A[-1]

# ans += tmp * 2 - 2 * tmp2
# print(ans)