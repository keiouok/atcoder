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

ans = [0] * N
for i in range(len(A)):
    ans[A[i]-1] = i + 1

print(*ans)


# L = []
# for i, a in enumerate(A):
#     L.append([i+1, a])
# L = sorted(L,key=lambda x: x[1])

# ans = []
# for i in range(N):
#     ans.append(L[i][0])
# print(*ans)

    