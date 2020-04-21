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
H = [INT() for i in range(N)]
tmp = 0
s = True
cnt = 0
ans = 0
for i in range(N):
    # print("H", H[i])
    # if s == True:
    if s == True and tmp < H[i]:
        tmp = H[i]
    if tmp > H[i]:
        tmp = H[i]
        s = False
    cnt += 1
    # else:
    if s == False and tmp < H[i]:
        # if tmp < H[i]:
        ans = max(ans, cnt)
        # print(cnt)
        cnt = 1
        tmp = H[i]
        s = True
    # print(cnt)
if s == True:
    cnt += 1
ans = max(ans, cnt)
print(ans)
            


