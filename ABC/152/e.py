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

# from functools import reduce
# from math import gcd as gcd_base  # from fractions import gcd
# gcd = lambda *numbers: reduce(gcd_base, numbers)  # 3 数以上の最大公約数

# lcm_base = lambda x, y: (x * y) // gcd_base(x, y)
# lcm = lambda *numbers: reduce(lcm_base, numbers, 1)  # 3 数以上の最小公倍数
# 最小公倍数
# def gcd(a, b):
#     if a < b:
#         a, b = b, a
#     while a % b != 0:
#         a, b = b, a % b
#     return b



def many_lcm(l):
    tmp = l[0]
    for i in range(1, len(l)):
        tmp = tmp * l[i]//gcd(tmp, l[i])
    return tmp
N = INT()
A = LIST()

lm = many_lcm(A)
ans = 0
for a in A:
    ans += lm // a
    
print(ans % mod)



