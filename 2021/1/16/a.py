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
B = LIST()
a = 0
b = 0

print(A[0] * B[0])
c = A[0] * B[0]
for i in range(1, N):
    a = max(a, A[i-1])
    b = max(b, B[i-1])
    c = max(a * B[i], A[i] * B[i], c)
    # print(max(max(a, A[i]) * B[i], a * b))
    print(c)
