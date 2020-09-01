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

N, H = MAP()
L = [LIST() for i in range(N)]

A = []
B = []
for a, b in L:
    A.append(a)
    B.append(b)

A.sort(reverse=True)
B.sort(reverse=True)

big_B = []

ma_A = max(A)
for b in B:
    if ma_A <= b:
        big_B.append(b)
thr = sum(big_B)
damage = 0 
cnt = 0
if thr >= H:
    for i in range(N):
        if damage < H:
            damage += B[i]
            cnt += 1
else:
    need_damage = H - thr
    cnt = len(big_B)
    if need_damage % A[0] == 0:
        cnt += need_damage // A[0]
    else:
        cnt += need_damage // A[0] + 1
print(cnt)
