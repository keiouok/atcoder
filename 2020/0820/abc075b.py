import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left, bisect_right

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

H, W = MAP()
C = [input() for i in range(H)]
C = ["0"*(W+2)] + ["0"+C[i]+"0" for i in range(H)] + ["0"*(W+2)]
Z = [[0] * (W + 2) for i in range(H + 2)]

def surround_plus(i, j, Z):
    dx = [0, 1, 1, 1, 0,-1,-1,-1]
    dy = [1, 1, 0,-1,-1,-1, 0, 1]
    for idx in range(8):
        Z[i + dx[idx]][j + dy[idx]] += 1
    return Z


for i in range(H + 2):
    for j in range(W + 2):
        if C[i][j] == "#":
            Z = surround_plus(i, j, Z)

A = [[""] * W for i in range(H)]

for i in range(1, H + 1):
    for j in range(1, W + 1):
        if C[i][j] != "#":
            A[i-1][j-1] = str(Z[i][j])
        else:
            A[i-1][j-1] = "#"
print(*["".join(a) for a in A], sep="\n")
