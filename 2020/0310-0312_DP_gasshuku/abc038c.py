import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left, bisect_right

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
A = LIST()

left = 0
comp = 0
num = 0
ruiseki = [1] * (N + 1)
for right in range(N-1):
    now = A[right]
    if now < A[right+1]:
        num += 1
        ruiseki[right+1] += ruiseki[right]
        now = A[right+1]
    else:
        # ruiseki[right]
        num = 0
#    else:
ruiseki.pop()
print(sum(ruiseki))
#        left = 
    
