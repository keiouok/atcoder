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

dic = {}
for i in range(N):
    if not A[i] in dic:
        dic[A[i]] = 1
    else:
        dic[A[i]] += 1

if N % 2 == 0:
    # even
    # N = 8
    for i in range(N//2):
        #4 (0, 1, 2, 3)
        if N - 1 - 2 * i not in dic:
            # 7, 5, 3, 1
            # なければでる
            print(0)
            # exit()
            break
        elif dic[N-1-2*i] != 2:
            print(0)
            break
        else:
            pass
    else:
        print(2 ** (N // 2) % mod)
else:
    if A.count(0) != 1:
        print(0)
        # exit()
    else:
        # N = 5
        for i in range(N//2):
            # 2, (0, 1)
            if N - 1 - 2 * i not in dic:
                print(0)
                break
            elif dic[N-1-2*i] != 2:
                print(0)
                break
            else:
                pass
        else:
            print(2 ** (N // 2) % mod)



exit()


flag = True
if N % 2 == 1:
    for i in range((N+1) // 2):
        if i == 0:
            if A.count(i) != 1:
                flag = False
        elif A.count(i * 2) != 2:
            flag = False
    if flag == False:
        print(0)
        exit()
    else:
        print(2 ** ((N-1) // 2))
else:
    for i in range(N // 2):
        if A.count(2 * i + 1) != 2:
            flag = False
    if flag == False:
        print(0)
    else:
        print(2 ** (N//2))
