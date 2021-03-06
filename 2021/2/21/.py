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

L = sorted(L)
A = []
for l in L:
    A.append(sum(l))
# print(A)
B = sorted(L, key=lambda x: x[0])
C = sorted(B, key=lambda x: x[1]) # 1番目の要素でソート
# q = deque(C)

D = sorted(L, key=lambda x: x[1])
E = sorted(D, key=lambda x: x[0])

# print(E, C)
# print(q)
# left, right = q.popleft()

ans = min(min(A) , max(C[0][0], C[1][1]), max(E[0][1], E[1][0]))
print(ans)