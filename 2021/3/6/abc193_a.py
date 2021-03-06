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
 
L = sorted(L)
A = []
for l in L:
    A.append(sum(l))
# print(A)
tmp1 = min(A)
q = deque(L)
# print(q)
# first is smallest

C = sorted(L, key=lambda x: x[1]) # 1番目の要素でソート
 
D = sorted(C, key=lambda x: x[0]) # 1番目の要素でソート

# print(C)
# print(D)
tmp2 = min(max(C[0][0], C[1][1]), max(C[1][0], C[0][1]))
tmp3 = min(max(D[0][0], D[1][1]), max(D[1][0], D[0][1]))
ans = min(tmp1, tmp2, tmp3)
# # print(L[0][0], L[1][1])
# ans = min(min(A) , max(C[0][0], C[1][1]), max(C[0][1], C[1][0]), max(1))
print(ans)