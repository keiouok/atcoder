import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from heapq import *

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

dic = defaultdict(list)
for i in range(N):
    a, b = MAP()
    dic[a].append((-1) * b)

ans = 0
incre = []

# M日後から1 ~ M日前
for i in range(1, M+1):
    for j in dic[i]:
        heappush(incre, j)
    if incre:# is exist 
        ans += -heappop(incre)
print(ans)


