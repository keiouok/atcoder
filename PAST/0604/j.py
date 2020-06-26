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

N, M = MAP()
A = LIST()

A = deque(A)
stomach = [0] * N
eaten = [-1] * M

i = 0
j = 0
flag = False
# while stomach[0] < A[j]:
#     stomach[0] = A[j]
ans = [0] * M
for m, a in enumerate(A):
    flag = False
    for n in range(N):
        if stomach[n] < a and flag == False:
            stomach[n] = a
            ans[m] = n + 1
            # print("s:", stomach)
            # print(ans)
            flag = True
    if ans[m] == 0:
        ans[m] = -1
print(*ans)
