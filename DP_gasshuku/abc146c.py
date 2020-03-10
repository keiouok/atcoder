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

A, B, X = MAP()

left = 0
right = 10 ** 9 + 1

def f(N):
    return A * N + B * len(str(N))

pre_mid = 0
mid = INF
while pre_mid != mid:
    pre_mid = mid
    mid = (right + left) // 2
    need = f(mid)
    if need <= X:
        left = mid
    else:
        right = mid
#print(mid)
print(left)
#print(right)


