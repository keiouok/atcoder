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
L = [LIST() for i in range(N)]

A_a = []
# for i in range()
A = []
B = []
for a, b in L:
    c = a % b
    A_a.append(c)
    B.append(b)
    A.append(a)

ruiseki = 0
cnt = 0
for i in range(N):
    amari = B[N-i-1] - ((A[N-i-1] + ruiseki) % B[N-i-1])
    if amari == B[N-i-1]:
        cnt += 0
        ruiseki += 0
    else:
        cnt += amari
        ruiseki += amari
    # print()
    # print("amari:", amari)
    # print(amari)
    # cnt += amari
print(cnt)

