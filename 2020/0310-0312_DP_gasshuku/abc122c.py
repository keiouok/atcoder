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

N, Q = MAP()
S = input()
L = [LIST() for i in range(Q)]
ruiseki = [0] * (N)

for i in range(N-1):
    if S[i+1] == "C" and S[i] == "A":
        #if S[i] == "A":
            ruiseki[i+1] += ruiseki[i] + 1
    else:
        ruiseki[i+1] = ruiseki[i]
for l, r in L:
    ans = ruiseki[r-1] - ruiseki[l-1]
    print(ans)

    

