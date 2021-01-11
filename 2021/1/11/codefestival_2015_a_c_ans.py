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
from decimal import Decimal

# 16:43-17:06
# 解説AC
N, T = MAP()
L = [LIST() for i in range(N)]
A = []
B = []
C = []
for a, b in L:
    A.append(a)
    B.append(b)
    C.append([a - b, a, b]) # 増える分 a - b

C.sort()

t = sum(B)
if T - t < 0:
    print(-1)
    exit()

a_cnt = 0

for d, a, b in C:
    t = t + d
    if t <= T:
        a_cnt += 1
print(N - a_cnt)
    