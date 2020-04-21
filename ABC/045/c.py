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

s = list(input())
# s = list(map(int, s))
from itertools import product
num = len(s)-1
bits = product([0, 1], repeat=num)
L = []
for x in bits:
    l = []
    r = [s[0]]
    for i in range(len(x)):
        if x[i] == 0:
            r.append(s[i+1])
        if x[i] == 1:
            l.append(r)
            r = []
            r.append(s[i+1])
    l.append(r)
    L.append(l)
# print(L)
ans = 0
for equ in L:
    # print(equ)
    for y in equ:
        # print(y)
        ans += int("".join(y))
print(ans)


    

