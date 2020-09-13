import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left, bisect_right

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, M, K = MAP()
A = LIST()
B = LIST()
A_ruiseki = A
B_ruiseki = B
for i in range(N-1):
    A_ruiseki[i+1] += A_ruiseki[i]

for i in range(M-1):
    B_ruiseki[i+1] += B_ruiseki[i]
ans = 0
for i in range(N):
    a_idx = 0
    # b_idx = 0
    amari = K
    if K - A_ruiseki[i] >= 0:
        a_idx = i + 1
        amari = amari - A_ruiseki[i]
        b_idx = bisect(B_ruiseki, amari)
        total = a_idx + b_idx
        ans = max(ans, total)
#  only b case
b_idx = bisect(B, K)
# print(b_idx)
ans = max(ans, b_idx)
print(ans)
