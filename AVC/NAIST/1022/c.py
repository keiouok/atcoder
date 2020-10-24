import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
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

ans = []
while 1:
    N, M = MAP()
    if N == 0 and M == 0:
        break
    A = LIST()
    B = []
    A.sort()
    mi = A[0] + A[1]
    ma = A[-1] + A[-2]
    if M < mi:
        ans.append("NONE")
        continue
    B = list(combinations(A, 2))
    tmp = INF
    for b in B:
        amari = M - sum(b)
        if amari >= 0:
            if tmp > amari:
                tmp = amari
                t = sum(b)
    ans.append(t)

print(*ans, sep="\n")    
