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

a, b, x, y = MAP()

# if a >= b:
# diff = abs(a - b)
diff = a - b
# if diff >= 0
if a >= b:
    diff = a - b
    if diff == 0:
        ans = x
    else:
        ans = min(x + y * (diff - 1), (diff * 2 - 1) * x)

else: # b > a
    diff = b - a
    if diff == 0:
        ans = x
    # elif diff % 2 != 0:
    ans = min(x + y * diff, (diff * 2 + 1) * x)
    #     if x <= y:
    #         ans = min(x + y * diff, x * (diff + 2))
    #         # x のみでいける
    #         # ans = x * diff
    #     else:
    #         # x ななめ のこりがy
    #         # ans = x + (diff - 1) * y
    # else:
    #     # even
    #     if x <= y:
    #         # ans = y + (diff - 1) * x
    #     else: # x > y
    #         # ans = x + (diff - 1) * y

print(ans)

        

