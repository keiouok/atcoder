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

N, M  = MAP()
A = LIST()
B = LIST()

a = 0
b = 0

# while 1:
#     if A[a] < B[a]:




memo = [0] * (10 ** 3 + 1)

for a in A:
    memo[a] += 1
for b in B:
    memo[b] += 1

ans = []
for i in range(10 ** 3 + 1):
    if memo[i] == 1:
        ans.append(i)
        # print(i, sep=" ")
print(*ans, sep=" ")