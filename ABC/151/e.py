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

# def power(x, y):
#     if y == 0:
#         return 1
#     elif y == 1:
#         return x % mod
#     elif y % 2 == 0:
#         return power(x, int(y/2)) ** 2 % mod
#     else:
#         return power(x, int((y-1)/2)) ** 2 * x % mod

# # nCaとしたときのaのmaxがa_max
# a_max = 10 ** 5
# # a, bの最大値+2
# fact = [1] * (a_max + 2)
# # 逆元
# for i in range(1, a_max + 1):
#     fact[i] = (fact[i-1] * i) % mod
# # combination
# def C(n, a):
#     tmp = 1
#     for i in range(n, n-a, -1):
#         tmp = (tmp * i) % mod
#     return tmp * power(fact[a], mod - 2)


upper = 10**5  # 必要そうな階乗の限界
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
 




N, K = MAP()
A = LIST()

A.sort()
# each max, min
max_wa = 0
min_wa = 0

for i in range(N-(K-1)):# N-(K-1)の範囲 
    # A[i]の値がmax,minになる集合SがnCk個ある．
    max_wa += A[N-1-i] * C(N-1-i, K-1)
    min_wa += A[i] * C(N-1-i, K-1)
print((max_wa - min_wa) % mod)




