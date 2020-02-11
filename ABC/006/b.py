import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

mod = 10007
n = INT()
a = [0, 0, 1]
if n <= 2:
    print(a[n-1])
    exit()
if n >= 3:
    for i in range(3, n):
        a.append((a[i-1] + a[i-2] + a[i-3])%mod)
print(a.pop())


# a = [0, 0, 1]
# if n <= 2:
#     print(a[n-1])
# else:
#     i = 3
#     while i != n-1:
#         a[i] = a[i-1] + a[i-2] + a[i-3]
#         i += 1
#         if i == n-1:
#             break
# print(a[n-1])



# a = [0] * (10 ** 6 + 1)
# a = [0, 0, 1]
# ans = 0
# def f(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 0
#     if n == 3:
#         return 1
#     else:
#         return f(n-1) + f(n-2) + f(n-3)
# print(f(n) % mod)

