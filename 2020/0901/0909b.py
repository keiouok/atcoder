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

N = INT()
A = [input() for i in range(N)]
M = INT()
B = [input() for i in range(M)]

# dic = dict()
dic = dict()

for a in A:
    dic[a] = 0
cnt = 0
for i in range(M):
    flag = True
    for j in range(N):
        if B[i] == A[j]:
            # if dic[B[i]] % 2 == 0:
            if cnt % 2 == 0:
                print("Opened by", A[j])
            else:
                print("Closed by", A[j])
            # dic[B[i]] += 1
            cnt += 1
            flag = False
            break
    if flag == True:
        print("Unknown", B[i])
    


