from collections import deque, defaultdict, Counter
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
import sys
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
a = N % 1000
# if 0 <= N < 1000:
#     print(N)
if N % 1000 == 0:
    print(0)
else:
    print(1000 - a)


# for i in range(1, 10+1):
#     have = 1000 * i

#     if 0 <= have - N < 1000:
#         print(have - N)
#         exit()
