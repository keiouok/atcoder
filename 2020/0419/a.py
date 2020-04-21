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

N, K = MAP()
A = [INT() for i in range(N)]

seki = 1
ans = 0
left = 0
right = 0

if 0 in A:
    print(N)
    exit()

for right in range(1, N+1):
    seki *= A[right-1]
    if seki <= K:
        ans = max(ans, right - left)
    else:
        left += 1
        seki //= A[left-1]
print(ans)




exit()
while right < N:
    seki *= S[right]
    if seki > K:
        # if left == 0:
        #     ans = max(ans, right)
        while seki > K:
            seki //= S[left]
            left += 1
    if seki <= K:
        ans = max(ans, right - left + 1)
        print(right, left)
        right += 1
print(ans)


