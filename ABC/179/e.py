import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, X, M = MAP()
ans = 0
flag = False
L = []
dic = dict()
for i in range(1, N+1):
    if X % M not in L:
        L.append(X % M)
    else:
        flag = True
        tmp = X % M
        l = len(L)
        break
    X = (X % M) ** 2
if flag == True:
    index = L.index(tmp)
    nR = L[:index]
    R = L[index:]
    amari = (N - len(nR)) % len(R)
    ans = sum(nR) + (N - len(nR)) // len(R) * sum(R) + sum(R[:amari])
    print(ans)    
else:
    ans = sum(L)
    print(ans)