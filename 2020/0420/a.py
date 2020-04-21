import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from heapq import heapify, heappop, heappush

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

L = [INT() for i in range(5)]
A = []
for l in L:
    A.append(ceil(l * 0.1) * 10)
# print(A)

ans = INF
for i in range(5):
    tmp = 0
    for j in range(5):
        if i == j:
            tmp += L[j]
        else:
            tmp += A[j]
    ans = min(tmp, ans)
print(ans)    