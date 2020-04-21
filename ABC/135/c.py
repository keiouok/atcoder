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

n = INT()
A = LIST()
B = LIST()
ans = sum(A)
for i in range(n):
    # while A[i] > 0:
    if A[i] <= B[i]:
        B[i] = B[i] - A[i]
        A[i] = 0

        # print(A)
        # print(B[i] - A[i])
        # print(B[i])
        # print(B)
        if A[i+1] <= B[i]:
            B[i] = B[i] - A[i+1]
            A[i+1] = 0

        else:
            A[i+1] = A[i+1] - B[i]
            B[i] = 0
            # print(A)
    else:
        A[i] = A[i] - B[i]
        B[i] = 0
        if A[i+1] <= B[i]:
            B[i] = B[i] - A[i+1]
            A[i+1] = 0

        else:
            A[i+1] = A[i+1] - B[i]
            B[i] = 0
    # print(A)
# print(A)
# print(A)
ans = ans-sum(A)
print(ans)

    





    # if A[i] > 0:
    #     B[i] -= 1
    #     A[i] -= 1
        
    # while(B[i] >= 0):
    #     B[i] = B[i] - A[i]

# for i in range(n):
#     if A[i] <= A[i+1]:
#         t = A[i+1]
#         c = A[i+1] - B[i]
#         c = max(0, c)
#         A[i+1] = c
#     else:
#         t = A[i]
#         c = A[i] - B[i]
#         c = max(0, c)
#         A[i] =c
# print(A)

