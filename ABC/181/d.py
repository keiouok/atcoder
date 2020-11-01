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

A = input()
N = int(A)

d = Counter(A)

B = list(A)
b = sorted(B)
c = sorted(B, reverse=True)
# print("".join(b), "".join(c))
b = "".join(b)
c = "".join(c)
ib = int(b)
ic = int(c)

c = deepcopy(d)

# index is num
ref = [0] * 10

for a in list(A):
    ref[int(a)] += 1
print(ref)

hyp = deepcopy(ref)

for i in range(ib + 1, ic + 1):
    ib_before = ib - 1
    # if i == ib:
    #     # reigai
    #     # 1234
    #     if hyp == ref:
    #         if i % 8 == 0:
    #             print("Yes")
    #             exit()
    # else:
        # 1235
    if str(ib_before)[]
    l = len(str(i))
    S = str(i)
    c = Counter(list(S))
    if c == d:
        if i % 8 == 0:
            print("Yes")
            exit()
#     print(S)
#     print(S[-4:])

#     u = int(S[-4:])
#     # ni = u // 2
#     ni = u // 2
#     print(ni)
#     b = str(ni)[-3:]
#     if int(b) % 4 == 0:
#         print("Yes")
#         exit()
print("No")
#     # print(c)
#     # if c == d:



