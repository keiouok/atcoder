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
c = sorted(c.items(), key=lambda x:x[0], reverse=True)
d = []
for a in c:
    # print(a)
    if a[1] >= 2:
        d.append(a)
# print(d)
d = sorted(d, key=lambda x:x[0], reverse=True)
squ = 0
for y in d:
    # print(y)
    if y[1] >= 4:
        squ = (y[0] ** 2)
    
    break
ans = squ

if len(d) >= 2:
    
    
# if len(d) >= 2:
    ans = (max(d[0][0] * d[1][0], ans))


print(ans)