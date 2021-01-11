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

# 11:40-11:52
X, K, D = MAP()

# k = X // D
ma = K * D

# 正化
if X < 0:
    X *= -1

if X >= ma:
    ans = X - ma
else:
    n = X // D
    rd = X % D
    ld = D - rd
    if n % 2 == K % 2:
        ans = rd
    else:
        ans = ld

print(ans)    

