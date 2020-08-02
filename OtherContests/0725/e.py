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

N = INT()
A = LIST()

mi = min(A)
ma = max(A)

for i in range(N):
    if mi == A[i]:
        mi_left = i

for i in range(N):
    if ma == A[N-i-1]:
        ma_right = N - i

B = A[mi_left:ma_right]
# print(B)
if len(B) == 0:
    print(1000)
    exit()
C = []
for i in range(len(B)-1):
    if B[i] == B[i+1]:
        continue
    C.append(B[i])
if B[-1] != B[-2]:
    C.append(B[-1])  

have = 1000
kabu_num = 0
for i, c in enumerate(C):
    if i % 2 == 0:
        if 0 <= i - 2 < len(C):
            if C[i-2] > C[i]:
                continue
        kabu_num += have // c
        have = have - kabu_num * c
    else:
        if 0 <= i - 2 < len(C):
            if C[i-2] > C[i]:
                continue
        have += kabu_num * c
        # kabu_num -= 
        kabu_num = 0

print(have)


