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

l = [LIST() for i in range(m)]
p = LIST()

# bits全探索
bits = product([0, 1], repeat=n)
ans = 0
#print(list(bits))

for b in bits:
    light = 0
    for i, s_l in enumerate(l):
        on = 0
        for s in s_l[1:]:
            on += b[s-1]
        if on % 2 == p[i]:
            light += 1
    if light == m:
        ans += 1

print(ans)
