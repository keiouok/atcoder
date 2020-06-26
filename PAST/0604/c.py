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

A, R, N = MAP()

ans = A
# ans = A * R ** (N-1)
# if R 
if R == 1:
    print(A)
    exit()
while N - 1 > 0:
    N -= 1
    ans = ans * R
    # print(ans)
    if ans > 10 ** 9:
        print("large")
        exit()
    # if ans == ans * R:
        # print()
else:
    print(ans)
