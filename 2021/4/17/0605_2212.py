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
T = LIST()

T.sort(reverse=True)
A = []
B = []
a, b = 0, 0

print(T)
ruiseki = deepcopy(T)
large = deepcopy(T)
small = sorted(T)
for i in range(N-1):
    large[i+1] += large[i]
    small[i+1] += small[i]

print(large)
print(small)

total = sum(T)
print(total)
thre = ceil(total / 2)
# print(thre)
ans = total
if total // 2 == total / 2:
    thre = total // 2
else:
    thre = ceil(total / 2) # 13
    # ちょうどいける半分の所

print(total)
ans = thre
for l in large:
    if l < thre - 1:
        # ありえない
        continue
    else:
        pass
        





# for t in T:
#     if a == 0:
#         a += t
#         A.append(t)
#     else:
#         if a >= b:
#             b += t
#             B.append(t)
#         else:
#             a += t
#             A.append(t)
# print(max(a, b))
# print(A)
