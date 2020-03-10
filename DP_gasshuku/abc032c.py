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
s = [INT() for i in range(N)]

ans = 0
left = 0
seki = 1

if 0 in s:
    print(len(s))
    exit()

for right in range(1, N+1):
#    t = s[left:right]
    seki *= s[right-1]
    if seki <= K:
        if ans < right-left:
            ans = right-left
        continue
    else:# when large
        left += 1
        seki /= s[left-1]
print(ans)

