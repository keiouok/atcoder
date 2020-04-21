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

a, b, x = MAP()
s = x / a
y = s * 2 / b
if y <= a:

  sha = sqrt(b**2 + y**2)
  rad = math.acos(y/sha)
  do = math.degrees(rad)
  print(do)

  # 場合分け，三角形ver, 台形ver
else:
  s = x/a
  y = (s * 2 / a) - b
  # print(y)
  sha = sqrt(a ** 2 + (b-y) ** 2)
  rad = math.acos((b-y)/sha)
  do = math.degrees(rad)
  print(90-do)
  # print(do)



