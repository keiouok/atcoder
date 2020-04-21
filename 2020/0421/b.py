import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from heapq import heapify, heappop, heappush

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

M = list(input())

S = [int(s) for s in M]
L = [0, 1] #生成する数字
num = 3 #生成するビット数
bit_list = list(product(["+", "-"], repeat=num))

tmp = 0
for b in bit_list:
    ans = 0
    # print(b)
    for i, o in enumerate(b):
        # print("I", o)
        if o == "+":
            if i == 0:
                ans = S[i] + S[i+1]
            else:
                ans += S[i+1]
        else:
            if i == 0:
                ans = S[i] - S[i+1]
            else:
                ans -= S[i+1]
    # print(ans)
    if ans == 7:
        tmp = b
        break
ans = ""
for i, c in enumerate(tmp):
    ans += M[i]
    ans += c
ans += M[-1] + "=7"
print(ans)

