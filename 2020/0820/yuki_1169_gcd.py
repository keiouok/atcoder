import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left, bisect_right
from functools import reduce

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()

L = [i for i in range(1, N+1)]
L.sort(reverse=True)
a = L.pop()
L = [a] + L
ans = []
long_L = L + L
for i in range(1, N+1):
    ans.append(L)
    # print(long_L.index(i))
    idx = long_L.index(i)
    a = long_L[idx:idx+N]
    a = a[N-i+1:] + a[:N-i+1]
    print(*a)
