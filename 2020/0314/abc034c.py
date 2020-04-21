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

upper = 10**6  # 必要そうな階乗の限界を入れる
factorial = [1]
for i in range(1, upper):
    factorial.append(factorial[i-1] * i % mod)
def power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x % mod
    elif y % 2 == 0:
        return power(x, int(y/2)) ** 2 % mod
    else:
        return power(x, int((y-1)/2)) ** 2 * x % mod
 
def C(n, r):
    return (((factorial[n] * x_inv[r]) % mod) * x_inv[n-r]) % mod
 
x_inv = [0] * upper
x_inv[-1] = power(factorial[-1], mod-2)
for i in range(upper-2, -1, -1):
    x_inv[i] = x_inv[i+1] * (i+1) % mod

W, H = MAP()
print(C(W-1+H-1, W-1))

