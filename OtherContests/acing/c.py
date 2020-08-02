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

N = INT()
def f(x, y, z):
    return x**2 + y**2 + z **2 + x * y + y * z + z * x

L = [0] * (N + 1)
thre =  ceil(sqrt(N)) + 1
# print(thre)
for x in range(1, thre+1):
    for y in range(1, thre + 1):
        for z in range(1, thre + 1):
            if f(x,y,z) <= N:
                L[f(x, y, z)] += 1
print(*L[1:], sep="\n")



