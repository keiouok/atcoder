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

N, X = MAP()
A = LIST()

ans = 0
tmp = sum(A)
for i in range(N-1):
    # 減らす分, 減らさなくてこともある
    a = max(A[i] + A[i+1] - X, 0)

    A[i+1] = max(0, A[i+1]-a)
    # A[i]で残り減らす必要ある分
    b = max(0, a - A[i+1])
# print(A)
# print(ans)
c = 0
if A[0] + A[1] > X:
    c = A[0] + A[1] - X
A[0] = A[0] - c
print(tmp-sum(A))