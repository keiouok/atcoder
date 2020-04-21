import sys, re, os, math
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

N, K = MAP()
A = LIST()
F = LIST()

A.sort(reverse=True)
F.sort(reverse=True)
print(A)
print(F)


while K != 0:

  A.sort(reverse=True)
  F.sort(reverse=True)
  top = []
  ans = A[0] * F[0]
  index = 0
  for i in range(len(A)):
    for j in range(len(F)):
      x = A[i]*F[j]
      top.append(x)
      if ans < x:
        index = i
        ans = max(x, ans)
  print(index)

  a_i = index

  if A[index] >= K:
    A[index] = A[index] - K
    K = 0
  else:
    A[index] = 0
    K = K - A[index]

print(top)
# top.append(A[0] * F[0])
# top.append(A[0] * F[1])
# top.append(A[1] * F[0])
# top.append(A[1] * F[1])

# for i in range(len(top)):
# 何番目が最大かインデックスを答える
print(top)
taisho = top[0]
index = 0
for i in range(len(top)):
  if taisho < top[i]:
    index = i
print(index)









# A.sort(reverse=True)
# F.sort(reverse=True)
# print(A)
# print(F)

# if sum(A) <= K:
#   print(0)

# else:
#   for i in range(N):
#     if K >= A[i]:
#       K = K - A[i]
#       A[i] = 0
#     else: # A[i] > K
#       A[i] = A[i] - K
#       K = 0
#   print(A)
#   A.sort()
  
#   print(A)
#   s = []
#   for i in range(len(A)):
#       s.append(A[i]*F[i])

#   print(s)
#   # if x >= 1:







