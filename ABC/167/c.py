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

N, M, X = MAP()
L = [LIST() for i in range(N)]

dp =[[0] * (1+M) for i in range(1+N)]

A = []
B = [0] * M
C = []
for l in L:
    c = l[0]
    C.append(c)
    A.append(l[1:])
    for i, a in enumerate(l[1:]):
        B[i] += a
# print(B)

for b in B:
    if b < X:
        print(-1)
        exit()

L = [0, 1] #生成する数字
num = N #生成するビット数
bit_list = list(product([0, 1], repeat=N))
# print(bit_list)
ma = INF
for bit in bit_list:
    bit = list(bit)
    # print(bit)
    # print(bit)
    l = [0] * M
    cost = 0
    for i, b in enumerate(bit):
        if b == 1:
            for m, a in enumerate(A[i]):
                l[m] += a
            cost += C[i]
    # print(l, cost)
    # print(l)
    cnt = 0
    for k, b in enumerate(l):
        if b >= X:
            cnt += 1
    if cnt == M:
        # print(l)
        # print(cost)
        ma = min(ma, cost)
print(ma)








# for i in range(1, N+1):
#     for j in range(1, M+1):
#         c = C[i]
#         if i - w