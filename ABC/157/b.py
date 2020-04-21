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

A = [LIST() for i in range(3)]
N = INT()
B = [INT() for i in range(N)]
T = [[False] * 3 for i in range(3)]

for i in range(3):
    for j in range(3):
        if A[i][j] in B:
            T[i][j] = True

# tate
for i in range(3):
    if T[i][0] == T[i][1] == T[i][2] == True:
        print("Yes")
        exit()
for i in range(3):
    if T[0][i] == T[1][i] == T[2][i] == True:
        print("Yes")
        exit()

if T[0][0] == T[1][1] == T[2][2] == True:
    print("Yes")
    exit()
if T[0][2] == T[1][1] == T[2][0] == True:
    print("Yes")
    exit()

print("No")

