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

# 12:02-12:14
N = INT()
K = LIST()

tmp = 0
L = []
L.append(K[0])
cnt = 0
for i in range(N-2):
    l = K[i]
    r = K[i+1]
    b = L[i]
    # if cnt % 2 == 0:
    L.append(min(l, r))
        # cnt += 1
    # elif cnt % 2 != 0:
        # L.append(max(l, r))
        # cnt += 1
L.append(K[-1])
print(*L, sep=" ")

        


