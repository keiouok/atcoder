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

a, b = MAP()

for i in range(1, 2000):
    tax8 = i * 8 // 100
    tax10 = i * 10 // 100
    if tax8 == a and tax10 == b:
        print(i)
        exit()
    
print(-1)
exit()
x1 = a / 0.08
y1 = b /0.1
x2 = (a+1) / 0.08
y2 = (b+1) /0.1


# exit()
if ceil(y1) <= ceil(x1) < y2:
    ans = ceil(x1)
    print(ans)
elif ceil(x1) <= ceil(y1) < x2:
    ans = ceil(y1)
    print(ans)
else:
    print(-1)

