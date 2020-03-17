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
B = [i for i in range(1, N + 1)]
C = [0] * N

r = 0
ans = 0
while r < N:
    if A[r] == r + 1:
        ans += 1
        r += 1
    r += 1
print(ans)


exit()
for i in range(N):
    if A[i] == B[i]:
        C[i] = 1

# for i in range(N-1):
r = 0
pre_is_one = False

# 1の連続数を数える
conti_one = []
# print(C)
while r < N:
    conti = 0
    while C[r] == 1:
        conti += 1
        r += 1
        # print(r)
        if r >= N:
            break

    conti_one.append(conti)
    # if C[r] == 1:
    #     ans += 1
    #     while C[r]
    #     r += 1
    #     if pre_is_one == True:
    #         ans -= 1
    #     pre_is_one = True
    if r < N and C[r] == 0:
        r += 1
    
# print(ans)
# print(conti_one)
ans = 0
for c in conti_one:
    # print(c)
    if c == 1:
        ans += 1
    elif c > 1:
        ans += c - 1
print(ans)

    