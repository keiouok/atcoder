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

S = input()
N = len(S)
tmp = 0
ans = 0
A = 0
B = 0
b_num = 0
for i in range(1, N+1):
    if S[i-1] == "B":
        b_num += 1
        A += i

all_wa = N * (N + 1) // 2
B = all_wa - (N - b_num) * (N - b_num + 1) // 2

print(B - A)