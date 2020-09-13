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

N = INT()
A = LIST()
dic = defaultdict(list)
A.sort(reverse=False)
first = A.popleft()
q = deque([])
cnt = 0
for i, a in enumerate(A):
    if i % 0 == 0:
        q.append(a)
    else:
        q.appendleft(a)

# q.append(first)
# q.appendleft(first)

# # while 1:
# ans = 0
# for i, y in enumerate(i, q):
#     if len(q) == 1:
#         ans += 1
#     else:
#         if i == 0:
#             # left


# for a in A:
#     if len(stack) == 0:
#         stack.append(a)
#         stack.append(a)
#     else:
#         if len(stack) == 1:
#             stack.append(a)
#         else:

    # dic[a].append()
    # dic[b].append()
    



