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

n, x = MAP()
A = LIST()

bin_str = format(x, "b")
zero_num = n - len(bin_str)
bin_str = "0" * zero_num + bin_str
# print(bin_str)

ans = 0
for i in range(n):
    sign = bin_str[n-1-i]
    if sign == "1":
        ans += A[i]
print(ans)