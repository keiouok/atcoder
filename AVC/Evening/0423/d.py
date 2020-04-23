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
A = LIST()
B = [0] * N # 入っている箱 0 1 0 1とか
wa = 0
tmp = 0
for i in range(N, 0, -1):
    tmp = 0
    for j in range(i, N+1, i):
        if i == j:
            continue
        else:
            # print(j)
            # ここだけ気を付けようね
            tmp ^= B[j-1]
    # print("*****")
    if tmp == A[i-1]:
        B[i-1] = 0
    else:
        B[i-1] = 1
# print(B)
M = sum(B)
if M == 0:
    print(M)
    exit()
else:
    print(M)
    for i, b in enumerate(B):
        if b == 1:
            print(i+1, end=" ")
    print()