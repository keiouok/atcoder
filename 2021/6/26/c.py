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


N = INT()
L = [LIST() for i in range(N)]
L.sort()
L_a = sorted(L, key=lambda x: x[1]) # 0番目の要素でソート

# print(L_a)
L_new = []

for i in range(N):
    if L[i][0] == 4:
        l = [L[i][1]+0.1, L[i][2]-0.1]
    elif L[i][0] == 3:
        l = [L[i][1]+0.1, L[i][2]]
    elif L[i][0] == 2:
        l = [L[i][1], L[i][2]-0.1]
    elif L[i][0] == 1:
        l = [L[i][1], L[i][2]]
    L_new.append(l)

L_new = sorted(L_new, key=lambda x: x[0]) # 0番目の要素でソート

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        # print(i, j)
        A_left, A_right = L_new[i]
        B_left, B_right = L_new[j]
        if A_left <= B_left <= A_right:
            cnt += 1
        else:
            continue
print(cnt)

