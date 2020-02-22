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

n, m = MAP()
x = 360 / 12 * n
y = 360  / 60 * m
z = 360 / 12 * m / 60

long = y % 360
# print(y)
# print(z)
short = (x+z) % 360
# print(long, short)
ans = max(long, short) - min(long, short)
ans =min(360 - ans, ans)
print(ans)

