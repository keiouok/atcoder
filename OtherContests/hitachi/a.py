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

a, b, m = MAP()
A = LIST()
B = LIST()
A_s = sorted(A)
B_s = sorted(B)
# print(A)
# print(B)
L = [LIST() for i in range(m)]

ans = A_s[0] + B_s[0]
for x, y, c in L:
    # print(x, y, c)
    v = A[x-1] + B[y-1] - c
    if ans > v:
        ans = v
print(ans)


# exit()


# D = [[0] * b for i in range(a)]
# for x,y,c in L:
#     D[x-1][y-1] = max(D[x-1][y-1], c)
# ans = INF
# C = [[0] * b for i in range(a)]
# for i in range(a):
#     for j in range(b):
#         ans = min(A[i] + B[j] - D[i][j], ans)
        
# print(ans)

# # exit()

# # for x, y, c in L:
# #     C[x-1][y-1] = min(C[x-1][y-1], C[x-1][y-1]-c)

# # print(min(C))


# # #     ans.append(A[x-1] + B[y-1] - c)
# # # print(min(ans))



# # exit()
# # s = input()
# # m= "hi"
# # # for i in range():
# # l = len(s) // 2
# # if l * m == s:
# #     print("Yes")
# # else:
# #     print("No")

# # # if s // 2

