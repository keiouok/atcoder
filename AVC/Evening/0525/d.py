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

N, X, Y = MAP()
dic = defaultdict(int)
for i in range(1, N+1):
    for j in range(1, N+1):
        tmp = min(abs(i - j), abs(X-i)+1+abs(j-Y), abs(Y-i)+1+abs(X-j))
        dic[tmp] += 1
for i in range(1, N):
    print(dic[i]//2)        

