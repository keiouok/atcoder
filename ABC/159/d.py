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
A = LIST()

c = Counter(A)
c_c = defaultdict(int)
for key, value in c.items():
    c_c[key] = value * (value - 1) // 2
wa = 0
for key, value in c_c.items():
    wa += value

ruiseki = [0] * N

for i in range(N):
    new_value = c[A[i]] - 1    
    ruiseki[i] = wa - c_c[A[i]] + new_value * (new_value - 1) // 2
    # value * (value - 1) // 2
    # c_c[A[i]]
print(*ruiseki, sep= "\n")
