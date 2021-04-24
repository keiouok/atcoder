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
B = LIST()

# for i, b in enumerate(B):
cnt = 0
# if N == 2:
#     print(B[-1] * 2)
#     exit()

# else:
for i in range(N-1):
    # print(B[i], B[i+1])
    if i == 0:
        cnt += B[0]
    else:
        # if B[i] <= B[i+1]:
        cnt += min(B[i-1], B[i])

print(cnt+B[-1])