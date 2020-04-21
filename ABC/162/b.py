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

N = INT()

ans = N * (N + 1) // 2
a = (N // 3) * (N // 3 + 1) // 2 * 3
b = (N // 5) * (N // 5 + 1) // 2 * 5
c = (N // 15) * (N // 15 + 1)  // 2 * 15
# print(ans, a, b, c)
print(ans - a - b + c)



# c = 0
# for i in range(1, N):
#     if i % 5 != 0 and i % 3 != 0:
#         c += i

# print(c)