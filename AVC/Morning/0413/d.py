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
X = LIST()

# dist = 0
s = []
l = []
s = deque(s)
l = deque(l)
for x in X:
    if x < 0:
        s.appendleft(-1 * x)
    else:
        l.append(x)
# s.sort()
# print(s, l)

left = 0
right = 0
q = []
ans = INF
for i in range(N-K+1):
    left = i
    right = i + K - 1
    ans = min(ans, min(abs(X[left]), abs(X[right])) + X[right] - X[left])
print(ans)
