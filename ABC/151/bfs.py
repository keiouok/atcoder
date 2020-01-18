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

# 最大公約数 
def gcd(a, b):
  if a < b:
      a, b = b, a
  while a % b != 0:
      a, b = b, a % b
  return b

# 最小公倍数
def lcm(a, b):
  y = a*b / gcd(a, b)
  return int(y)

n, m = MAP()


L = []
for i in range(m):
  l = S_LIST()
  L.append(l)

# wa

wa = [0] * n
ac = [0] * n


for i in range(m):
  p = int(L[i][0])-1
  ans = L[i][1]
  if ans == "WA":
    # まだacない
    if ac[p] == 0:
      wa[p] = wa[p] + 1
  # acあった
  if ans == "AC":
    ac[p] = 1

for i in range(n):
  if ac[i] == 0:
    if wa[i] > 0:
      wa[i] = 0


print(sum(ac), sum(wa))


# for p in range(1, n+1):
#   if L[i][0] == str(p):
#     for i in range(m):
#       if L[i][1] == "WA":
#         wa += 1

#     for i in range(m):
#       if L[i][1] == "AC":
#         ac += 1
#   print(wa)
#   print(ac)

  