import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from heapq import heapify, heappop, heappush
from bisect import bisect_right

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, M = MAP()
A = LIST()
L = [LIST() for i in range(M)]
dic = defaultdict(int)

# for a, b in L:
    # dic[A[a]] = b
A.sort()
L = sorted(L, key=lambda x : x[1], reverse=True)
# print(L)
i = 0
# for i, a in enumerate(A):
for f, t in L:
    while f > 0 and i < N:
        if t > A[i]:
            A[i] = t
            f -= 1
            i += 1
        else:
            print(sum(A))
            exit()
print(sum(A))
    
    