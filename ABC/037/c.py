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

N, K = MAP()
A = LIST()
ruiseki = []
ruiseki.append(sum(A[0:K]))
for i in range(N-K+1):
    if i != 0:
        ans = 0
        ans = ruiseki[i-1]+A[i+K-1]-A[i-1]
        ruiseki.append(ans)
print(sum(ruiseki))

