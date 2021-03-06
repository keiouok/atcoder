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

n, a, b = MAP()

def power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x % mod
    elif y % 2 == 0:
        return power(x, int(y/2)) ** 2 % mod
    else:
        return power(x, int((y-1)/2)) ** 2 * x % mod
ans = power(2, n) - 1
    
# nCaとしたときのaのmaxがa_max
a_max = 2 * 10 ** 5
# a, bの最大値+2
fact = [1] * (a_max + 2)
# 逆元
for i in range(1, a_max + 1):
    fact[i] = (fact[i-1] * i) % mod
# combination
def C(n, a):
    tmp = 1
    for i in range(n, n-a, -1):
        tmp = (tmp * i) % mod
    return tmp * power(fact[a], mod - 2)

print((ans - C(n, a) - C(n, b)) % mod)
