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

# def multiplyList(myList) : 
#     # Multiply elements one by one 
#     result = 1
#     length = len(myList)
#     if length == 0:
#         return 0
#     else:
#         for x in myList: 
#             result = result * x  
#         return result  

N, K = MAP()
L = [INT() for i in range(N)]
A = deque([])
longest = 0
seki = 1

if 0 in L:
    print(N)
    exit()

for right in range(N):
    A.append(L[right])
    seki *= L[right]
    while seki > K and len(A) != 0:
        seki /= A.popleft()
    # print(seki)
    longest = max(len(A), longest)
print(longest)

