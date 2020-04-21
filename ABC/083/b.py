import sys, re
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
# def LIST(): return list(map(int, input().split()))
# def LIST(): return list(map(str, input().split()))
def LIST(): return list(input())

sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

A, B = MAP()
S = LIST()
flag = False
if len(S) == A + B + 1:
    if S[A] == "-":
        for i in range(A):
            if S[i] != "-":
                for j in range(B):
                    if S[-1-j] != "-":
                        flag = True
if flag == True:
    print("Yes")
else:
    print("No")

# 15:51
