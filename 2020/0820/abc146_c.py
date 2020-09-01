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

A, B, X = MAP()

left = 1
right = 10 ** 9 + 1
def f(N):
    return A * N + B * len(str(N))

while 1:
    left_money = f(left)
    right_money = f(right)
    if X <= right_money:
        right = right // 2 + 1
    # elif X >= right_money:
    #     left = right
    if right == left:
        break

print(right, left) 





    
