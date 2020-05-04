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

N = INT()
A = LIST()
is_zero = False
if 0 in A:
    is_zero = True
minus = 0
plus = 0

for a in A:
    if a < 0:
        minus += 1
    elif a > 0:
        plus += 1    
ans = 0
for a in A:
    ans += abs(a)
tmp = INF
if is_zero == True or minus % 2 == 0:
    print(ans)
else:
    for a in A:
        if abs(a) < tmp:
            tmp = abs(a)
    print(ans - 2 * tmp)



    