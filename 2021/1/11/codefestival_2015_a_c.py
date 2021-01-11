import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
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
from decimal import Decimal

# 16:43-
N, T = MAP()
L = [LIST() for i in range(N)]
L = sorted(L, key=lambda x: x[1]) # 1番目の要素でソート
L = sorted(L, key=lambda x: x[0])
# print(L) 
flag = True
tmp = 0
cnt = 0
A = []
B = []
for a, b in L:
    A.append(a)
    B.append(b)
    if T - a >= 0:
        T -= a
    elif T - b >= 0:
        T -= b
        cnt += 1
    else:
        print(-1)
        flag = False

if flag == False:
    print(A, B)
    A_ruiseki = deepcopy(A)
    B_ruiseki = deepcopy(B)
    for i in range(N - 1):
        A_ruiseki[i+1] += A_ruiseki[i]
        B_ruiseki[i+1] += B_ruiseki[i]
    print(A_ruiseki)
    print(B_ruiseki)




print(cnt)