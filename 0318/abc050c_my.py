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
 
# 20:16
N = INT()
A = LIST()
 
flag = True
# A.sort()
 
# dic = {}
dic = defaultdict(int)
for i in range(N):
    if not A[i] in dic:
        dic[A[i]] = 1
    else:
        dic[A[i]] += 1
s = sum(A)
 
 
if N % 2 == 1:
    for i in range(N):
        if i == 0:
            if dic[i] != 1:
                flag = False
        elif i % 2 == 0:
            if dic[i] != 2:
                flag = False
        else:
            if dic[i] != 0:
                flag = False
        # elif dic[i * 2] != 2:
        #     flag = False
    if flag == False:
        print(0)
    else:
        if N == 1:
            print(1)
        else:
            print(2 ** ((N) // 2) % mod)
 
else:
    for i in range(N):
        if (i - 1) % 2 == 0:
            if dic[i] != 2:
                flag = False
        else:
            if dic[i] != 0:
                flag = False
    if flag == False:
        print(0)
    else:
        print(2 ** (N//2) % mod)
 
 
 
 
 
 
        
 
 
    # c = Counter(A)
    # c = sorted(c.items(), key=lambda x: x[0], reverse = False)
    # if c[0][1] != 1:
        # print(0)
    # for i in c[1:]:
        # if c[0]