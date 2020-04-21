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

T = INT()
N = INT()
A = LIST()
M = INT()
B = LIST()

if N < M:
    print("no")
else:
    # 人に関して，どのたこ焼きが売れるかどうかを順に見ていく．
    # たこ焼きが全部なくなればyesになる．
    for i in range(len(B)): # okyakusan
        for j in range(len(A)):# takoyaki
            if A[j] <= B[i] <= A[j] + T:
                A.pop(j)
                break
        else:
            print("no")
            exit()
        
    print("yes")