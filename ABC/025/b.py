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

N, A, B = MAP()
L = [S_LIST() for i in range(N)]

place = 0
v = 0
for s, d in L:
    d = int(d)
    if d < A:
        v = A
    elif A <= d < B:
        v = d
    else:
        v = B
    if s == "West":
        place -= v
    elif s == "East":
        place += v
if place < 0:
    print("West", abs(place))
elif place == 0:
    print(0)
else:
    print("East", place)
        
