import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, floor
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

n = INT()
A = LIST()
a = 0
ans = INF

for i in range(-100, 101):
    a = 0
    for j in range(n):
        a += (A[j]-i) ** 2

    ans = min(ans, a)
print(ans)

    





exit()
ave = sum(L)/n
if ave == int(ave):
    print(int(ave))
    a = ave
    for i in range(n):
        ans += (L[i] - a) ** 2
    print(int(ans))
    exit()
left = 0
if ave != int(ave):
    for i in range(n):
        if L[i] < ave:
            left = i + 1
    print(left)
    right = n - left
    if left < right:
        a = ceil(ave)
    else:
        #print(floor(ave))
        a = floor(ave)
    print(a)
    for i in range(n):
        ans += abs(L[i] - a) ** 2
    print(ans)
