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

N, M = MAP()
if N == 1 and M == 1:
    print(1)
elif N == 1:
    print(M - 2)
elif M == 1:
    print(N - 2)
else:
    print((N - 2) * (M - 2))


#A = [[0] * W for i in range(H)]
#C = ["o" * W for i in range(H)] 
#C = ["#"*(W+2)] + ["#"+C[i]+"#" for i in range(H)] + ["#"*(W+2)]
#dx = [1, 1, 0, -1, -1, -1, 0, 1]
#dy = [0, 1, 1, 1, 0, -1, -1, -1]
#
#for h in range(H):
#    for w in range(W):
#        for i in range(8):
#            if C[h+1+dx[i]][w+1+dy[i]] == "o":
#                A[h][w] += 1
#ans = 0
#for h in range(H):
#    for w in range(W):
#        if A[h][w] % 2 == 0:
#            ans += 1
#
#print(ans)
