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

# kanzenni rikai

tmp_A = [0] * N

for i, x in enumerate(A):
    if i % 2 == 0:
        tmp_A[i] = x
    else:
        tmp_A[i] = -x
# print(tmp_A)
x1 = sum(tmp_A)
tmp = x1
ans = []
for i in range(N):
    # print(int(tmp*2), end=" ")
    print(int(tmp), end=" ")
    tmp = 2 * A[i] - tmp
