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

S = list(input())
c = Counter(S)
# print(c)
d = dict()
L = ["A", "B", "C", "D", "E", "F"]
for l in L:
    d[l] = 0
# print(d)
for s in S:
    d[s] += 1
ans = []
for l in L:
    ans.append(d[l])
print(*ans)

# for key, value in c.items():
#     print(d[key])
#     d[key] += d[key] + 1
# print(d)
