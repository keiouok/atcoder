import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
 
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
#ball
X = [0] * (N + 1)
for i in range(N, 0, -1):
    # num = i+1
    tmp = A[i-1]
    # ここから上のボール
    for j in range(i, N+1, i):
        #これなかった
        if j == i:
            continue
        # AではなくボールXと
        # tmp ^= A[j-1]
        tmp ^= X[j]
    # X[i] = tmp ^ A[i]
    X[i] = tmp
    
    # if tmp == 0:
    #     X[i] = 0
    # else:
    #     X[i] = 1
# print(X)
# if sum(X) == 0:
#     print(sum(X))
#     exit()
print(sum(X))
ans = []
for i in range(N):
    if X[i+1] == 1:
        ans.append(i+1)
print(*ans)
