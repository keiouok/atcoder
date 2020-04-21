import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(float, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
L = [LIST() for i in range(N)]
l = [0] * 6
for high, low in L:
    if high >= 35:
        l[0] += 1
    if 30 <= high < 35:
        l[1] += 1
    if 25 <= high < 30:
        l[2] += 1
    if 25 <= low:
        l[3] += 1
    if low < 0 and 0 <= high:
        l[4] += 1
    if high < 0:
        l[5] += 1

print(*l)



