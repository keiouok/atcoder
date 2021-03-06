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

N, A, B, C = MAP()
l = [INT() for i in range(N)]

def dfs(idx, a, b, c):
    if idx == N:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else INF
    ret0 = dfs(idx+1, a, b, c)
    ret1 = dfs(idx+1, a + l[idx], b, c) + 10
    ret2 = dfs(idx+1, a, b + l[idx], c) + 10
    ret3 = dfs(idx+1, a, b, c + l[idx]) + 10
    return min(ret0, ret1, ret2, ret3)
if __name__ == "__main__":
    print(dfs(0, 0, 0 ,0))