import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
import itertools

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

# # 最小公倍数
# def gcd(a, b):
#   if a < b:
#       a, b = b, a
#   while a % b != 0:
#       a, b = b, a % b
#   return b
 
# 最大公約数 
def lcm(a, b):
  y = a*b / gcd(a, b)
  return int(y)

n, m = MAP()
A = LIST()
l = []
B = []
for a in A:
  B.append(a//2)

print(B)
for i in range(n):
  
  # print(B[i])
  # print(B[i+1])
  if i == 0:
    a = lcm(1, B[i])
  else:
    a = lcm(a, B[i])
  print(a)
print(1000000000 // a)



# print(gcd(5, 5))
# pr@int(B)







exit()
for x in range(1, m+1):
  flag = False
  for a in A:
    p = x / a - 0.5
    # print(p)
    # if p < 0:
    #   flag == False
    if p >= 0:
      if (int(p) - p) == 0:
        flag == True
        l.append(x)

    # if flag == True:
    # if flag == False:
    #   continue

c = Counter(l)
print(c)
count = 0
for k in c:
  if c[k] == n:
    count += 1
print(count)

      
    
        # l.append(p)
# print(l)   
  # for a in A:
  #   x = a * (p + 0.5)

