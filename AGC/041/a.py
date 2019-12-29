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

# 最小公倍数
def gcd(a, b):
  if a < b:
      a, b = b, a
  while a % b != 0:
      a, b = b, a % b
  return b
 
# 最大公約数 
def lcm(a, b):
    y = a*b / gcd(a, b)
    return int(y)

# N = INT()
# print(N)
N, A, B = MAP()
# guusuu
if (A - B) % 2 == 0:
  s = B - A
  ans = s // 2
  print(ans)
# kisuu
else:
  # if N - A <= B
  # k = B - A
  # m = min(N - A, B)
  if A - 1 <= N - B:
    # A ni tikazuku
    # 最初の移動
    s = A - 1
    # Bが残り移動する距離
    b = B - (A - 1) - 1

    ans = s + (b + 1) // 2
    # print(ans)
  else:
    s = N - B
    a = N - (A + s) + 1
    ans = s +  a // 2
    # ans = A + s + 1
    # ans = ans // 2
  print(ans)
  #   ans =(B - A + 1)//2

  # else:
  #   a = N - (A +  N - B )
  #   ans = a // 2
  # print(ans)
    



  # print(ans - k)
  # if A <= N - B:
  #   print(B - A)
  # else:
  #   print(B - A)
  # # k = B - A
  # ans = k+min(N - A, N - B)
  # B - min(N - A, N - B)
  # print(ans)


