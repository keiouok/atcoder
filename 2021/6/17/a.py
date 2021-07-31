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

from_left_zero = 0
from_left_one = 0

total_light = sum(A)
ans = total_light
left_one = 0
for i in range(N):
    left_one += A[i]
    left_zero = i - left_one + 1
    right_one = total_light - left_one
    right_zero = N - (i + 1) - right_one
    if left_zero <= left_one:
        # tsukeru
        left_time = left_zero
    else:
        left_time = left_one
    
    tmp = right_one + left_time
    ans = min(tmp, ans)
print(ans)