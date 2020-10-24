import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, log
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
# s = 18 /(1 - log(2, 10))
# print(s)
# m = log(N, 5) + 1
# print(m)

for b in range(1, 26):
    for a in range(1, 40):
        n = 3 ** a + 5 ** b
        if n == N:
            print(a, b)
            exit()
print(-1)

#     c = N - 5 ** b
#     # print(c)
#     if c > 0:
#         a = log(c, 3)
#         if a > 0 and a == int(a):
#             print(int(a), b)
#             exit()
#     else:
#         print(-1)
#         exit()
# print(-1)





# for b in range(int(sqrt()))




# for b in range(int(sqrt(N)) + 1):
#     if N - 5 ** b > 0:
#         a = log(N - 5 ** b, 3)
#         if int(a) == a:
#             print(int(a), b)
#             exit()
# print(-1)
        

#     amari = N - 3 ** a
#     if amari >= 0:
#         p = prime_decomposition(amari)
#         s = set(p)
#         # print(s)
#         if len(s) == 1:
#             # print(list(s)[0])
#             if list(s)[0] == 5:
#                 B = len(p)
#                 A = a
#                 print(A, B)
#                 exit()
#                 # A = N - 5 ** B

# print(-1)
            