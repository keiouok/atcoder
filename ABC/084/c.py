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
CSF = [LIST() for i in range(N-1)]

for i in range(N):
    time = 0
    for j in range(i, N-1):
        if time < CSF[j][1]:
            time = CSF[j][1]
        elif time % CSF[j][2] == 0:
            pass
        else:
            time += CSF[j][2] - time % CSF[j][2]
        time += CSF[j][0]
    print(time)


