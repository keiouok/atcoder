import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left
 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, D, K = MAP()
L = [LIST() for i in range(D)]
S = [LIST() for i in range(K)]

now = [0] * (K+1)

clear = [False] * (K+1)
clear[0] = True
day = 0

i = 0
for s, t in S:
    i += 1
    now[i] = s

for l, r in L:
    i = 0
    day += 1
    for s, t in S:
        i += 1
        if clear[i] == False:
            if l <= now[i] <= r:
                if l <= t <= r:
                    clear[i] = day
                elif t < l:
                    now[i] = l
                elif r < t:
                    now[i] = r
print(*clear[1:], sep="\n")


