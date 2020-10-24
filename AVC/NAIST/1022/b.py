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
ans = []
while 1:
    N = INT()
    if N == 0:
        break
    L = S_LIST()
    q = deque(L)
    cnt = 0
    for i in range(N-1):
        if L[i] == "ru":
            if L[i+1] == "lu":
                cnt += 1
        elif L[i] == "lu":
            if L[i+1] == "ru":
                cnt += 1

        elif L[i] == "rd":
            if L[i+1] == "ld":
                cnt += 1
        elif L[i] == "ld":
            if L[i+1] == "rd":
                cnt += 1
                


    # s = q.popleft()
    # while q:
    #     if s == "ru":
    #         print("1:", s)
    #         s = q.popleft()
    #         if s == "lu":
    #             cnt += 1
    #     elif s == "lu":
    #         print("2:", s)
    #         s == q.popleft()
    #         if s == "ru":
    #             cnt += 1
    #     elif s == "ld":
    #         print("3:", s)
    #         s = q.popleft()
    #         if s == "rd":
    #             cnt += 1
    #     elif s == "rd":
    #         print("4:", s)
    #         s = q.popleft()
    #         if s == "ld":
    #             cnt += 1
    ans.append(cnt)
        
print(*ans, sep="\n")        


        




