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
# ball を入れたら1
ball = [0] * (N+1)
for i in range(N, 0, -1):
    tmp = A[i-1]
    for j in range(i, N+1, i):
        if j == i:
            continue
        tmp ^= ball[j]
    # 辻褄合わせるためにはこれが必要
    ball[i] = tmp
print(sum(ball))
for i, b in enumerate(ball):
    if b == 1:
        print(i, end=" ")
    
    
