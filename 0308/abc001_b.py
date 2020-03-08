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

M = INT()
if M < 100:
    ans = 0
elif 100 <= M <= 5000:
    km = M / 1000
    ans = 10 * km
    # ans = str(ans).zfill(2)
elif 6000 <= M <= 30000:
    km = M / 1000
    ans = 50 + km
elif 35000 <= M <= 70000:
    km = M / 1000
    ans = (km - 30) / 5 + 80
elif 70000 < M:
    ans = 89
print(str(int(ans)).zfill(2))