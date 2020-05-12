import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from heapq import heapify, heappop, heappush
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

def lcm(a, b):
    y = a*b / gcd(a, b)
    return int(y)


A, B, C, D = MAP()
# print(gcd(C, D))
def f(N):
    a = N // C
    b = N // D
    c = N // lcm(C, D)
    # print(a, b, c)
    return N - (a + b - c)
print(f(B)-f(A-1))
# print(f(B))
# print(f(A-1))