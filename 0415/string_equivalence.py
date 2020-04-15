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
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
S = "abcdefghijk"

# q = [("", -1)]
ans = 0

def dfs(a, mx):
    # q = [(cur, mx)]
    # while q:
    # a, mx = q.pop()
    if len(a) == N:
        print(a)
        return
    for c in range(len(S[:mx+2])):
        t = a
        t += S[:mx+2][c]
        dfs(t, max(c, mx))

dfs("", -1)

