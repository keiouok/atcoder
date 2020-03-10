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

N, M = MAP()
L = [LIST() for i in range(M)]
P = LIST()

import itertools
#L = [0, 1] #生成する数字
num = N #生成するビット数
bit_list = list(itertools.product([0, 1], repeat=num))
#print(bit_list)
ans = 0
#print(L[0][0])
on = 0
for bit in bit_list:
    # ココ注意
    cnt = 0
    for i in range(M):
        #print(L[i][1:])
        wa = 0
        on = 0
        for s in L[i][1:]:
            on ^= bit[s-1]
        # wa == P[i]なら，その電球は点灯する
        if P[i] == on:
            cnt += 1
        #if cnt == L[i][0]:
        #    c += 1
    if cnt == M:
        ans += 1
print(ans)
