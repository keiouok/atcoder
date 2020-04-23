import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop, heapify
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, M = MAP()
A = LIST()
L = [LIST() for i in range(M)]

L = sorted(L, key=lambda x: x[1], reverse=True) # 0番目の要素でソート
default_sum = sum(A)
# A.sort()
heapify(A)
n = 0
for times, num in L:
    cnt = 0
    while cnt < times and len(A) != 0:
        min_num = heappop(A)
        default_sum += max(num - min_num, 0)
        cnt += 1
print(default_sum)




    

