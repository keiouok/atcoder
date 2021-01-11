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

# 17:09
x, y = MAP()

if x * y < 0:
    ans = 1 + abs(abs(x) - abs(y))
elif x == 0 or y == 0:
    if x < y:
        ans = max(abs(x), abs(y))
    else:
        ans = max(abs(x), abs(y)) + 1
else:
    # 正負一緒
    if y > x:
        ans = y - x
    else:
        # print(2 + abs(abs(x) - abs(y)))
        # print(2 + x - y)
        ans = 2 + x - y
print(ans)