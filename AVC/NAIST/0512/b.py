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

A, B = MAP()

def bigger(N):
    a_s = list(str(N))
    a_s = [int(a) for a in a_s]
    for i in range(3):
        if a_s[i] != 9:
            a_s[i] = 9
            break
    a_s = [str(a) for a in a_s]
    a_s = int("".join(a_s))
    return a_s
def smaller(N):
    a_s = list(str(N))
    a_s = [int(a) for a in a_s]
    for i in range(3):
        if i == 0:
            if a_s[i] != 1:
                a_s[i] = 1
                break
        else:
            if a_s[i] != 0:
                a_s[i] = 0
                break
    a_s = [str(a) for a in a_s]
    a_s = int("".join(a_s))
    return a_s

print(max(bigger(A) - B, A - smaller(B)))

    