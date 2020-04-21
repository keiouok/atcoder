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

A, B = MAP()

def f(x):
    if x % 2 == 1:
        # one_num
        tmp = (x + 1) / 2
        if tmp % 2 == 0:
            return 0
        else:
            return 1
    else:
        return f(x-1) ^ x
print(f(A-1) ^ f(B))

exit()
if A % 2 == 0 and B % 2 != 0:
    dist = B - A
    one_num = dist // 2 + 1
    if one_num % 2 == 0:
        ans = 0
    else:
        ans = 1
if A % 2 == 0 and B % 2 == 0:
    dist = B - 1 - A
    one_num = dist // 2 + 1
    if one_num % 2 == 0:
        ans = 0
    else:
        ans = 1
    ans = ans ^ B
if A % 2 != 0 and B % 2 != 0:
    dist = B - (A + 1)
    one_num = dist // 2 + 1
    if one_num % 2 == 0:
        ans = 0
    else:
        ans = 1
    ans = ans ^ A
if A % 2 != 0 and B % 2 == 0:
    dist = B - 1 - (A + 1)
    one_num = dist // 2 + 1
    if one_num % 2 == 0:
        ans = 0
    else:
        ans = 1
    ans = ans ^ A ^ B


print(ans)



