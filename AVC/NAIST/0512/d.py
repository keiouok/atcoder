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
C = [input() for i in range(N)]
cnt = 0
W = 9
H = N
for w in range(W):
    for h in range(H):
        if C[h][w] == "x":
            cnt += 1
        elif C[h][w] == "o":
            if h + 1 >= H:
                cnt += 1
            elif C[h+1][w] == "x" or C[h+1][w] == ".":
                cnt += 1
print(cnt)


        
