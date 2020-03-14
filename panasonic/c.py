import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left, bisect_right

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))

sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

a, b, c = MAP()
# s = c ** 2 + a ** 2 + b ** 2 - 2 * a * c - 2*b*c + 2 * a * b  - 4 * a - 4 * b
# if 0 < s:
if c - (a + b) > 0:
    if 4 * a * b < ((c - (a + b))) ** 2:
        print("Yes")
        exit()

print("No")

# exit()
# if sqrt(a * b) < (c - (a + b ))/2:
#     print("Yes")
# else:
#     print("No")

# exit()
# if sqrt(a) + sqrt(b) < sqrt(c):
#     print("Yes")
# else:
#     print("No")