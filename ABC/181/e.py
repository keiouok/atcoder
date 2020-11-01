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

memo = [0] * 10
for a in list(A):
    memo[int(a)] += 1

# B = list(A)
# b = sorted(B)
# c = sorted(B, reverse=True)
# print("".join(b), "".join(c))
# ib = int(b)
# ic = int(c)

if len(A) == 1:
    if int(A) == 8:
        print("Yes")
        exit()
elif len(A) == 2:
    if int(A[0] + A[1]) % 8 == 0 or int(A[1] + A[0]) % 8 == 0:
        print("Yes")
        exit()
else:
    for i in range(104, 1000, 8):
        tmp = [0] * 10
        l = list(str(i))
        c = Counter(l)
        if d[l[0]] >= c[l[0]] and d[l[1]] >= c[l[1]] and d[l[2]] >= c[l[2]]:
            print("Yes")
            exit()
        # Counter(A)
    # # L = set(list(combinations(list(A), 3)))
    # for l in L:
    #     a = list(permutations(l))
    #     for y in a:
    #         shimo = int("".join(y))
    #         if shimo % 8 == 0:
    #             print("Yes")
    #             exit()
    # #         if shimo % 2 != 0:
    # #             continue
    # #         ni = shimo // 2
    # #         b = int(str(ni)[-3:])
    # #         if b % 4 == 0:
    # #             print("Yes")
    # #             exit()
print("No")
