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

N, C, K = MAP()
T = [INT() for i in range(N)]
tmp = 0
cnt = 0
sa = [0] * N

for i in range(N-1):
    sa[i+1] = T[i+1] - T[i]
print(sa)
tmp = 0
for i in range(N):
    if cnt < C:
        if tmp < 
        tmp += sa[i]



    


