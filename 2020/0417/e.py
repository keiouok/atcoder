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
A = LIST()

left = 0
right = 0
left_wa = 0
right_wa = 0
wa = 0
ans = 0
for i in range(N):
    right_wa += A[i]
    wa = right_wa - left_wa
    if wa >= K:
        # while right_wa - left_wa >= K:
        while wa >= K:
            left_wa += A[left]
            wa = right_wa - left_wa
            left += 1
    
    ans += left
print(ans)            