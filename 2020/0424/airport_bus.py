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

N, C, K = MAP()
A = [INT() for i in range(N)]
num = 0
A.sort()
B = []
ans = 0
mi = 0
# print(A)
for i in range(N):
    if len(B) == C:
        # 超えていたら
        B = [A[i]]
        ans += 1
        mi = A[i]
    elif len(B) == 0:
        B = [A[i]]
        mi = A[i]
    else:
        gap = A[i] - mi
        if gap <= K:
            B.append(A[i])
        else:
            B = [A[i]]
            ans += 1
            mi = A[i]
    # print(B)
if len(B) != 0:
    ans += 1
print(ans)
            
    
