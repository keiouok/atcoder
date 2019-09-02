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

# a, b = MAP()
# n = INT()
# a, b, c = MAP()
n = INT()
H = LIST()
R = [0]*n
for i in range(n-1):
    if H[i] >= H[i+1]:
        R[i+1] = R[i]+1
print(max(R))
        
    # while(1):

    # for j in range(n):
