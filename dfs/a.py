# あけおめ，昨日の復習です．
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

# まわりを#で囲む
def surround(C): # Cはリスト 
  H = len(C)
  W = len(C[0])
  D = []
  first = ["#"] * (W + 2)
  D.append(first)
  for h in range(H):
    # for w in range(W):
    C[h].append("#")
    C[h].insert(0, "#")
    D.append(C[h])
  D.append(first)
  return D

# default
cx, cy = 0, 0
sx, sy = 0, 0
gx, gy = 0, 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(cx, cy):
  if cx == gx and cy == gy:
    return True
  else:
    data[cy][cx] == "#"
    for d in range(4):
      nx = cx + dx[d]
      ny = cy + dy[d]
    if data[ny][nx] != "#":
      f = dfs(nx, ny)
      if f == True:
        return True
  return False

H, W = MAP()
data = []
for i in range(H):
  d = list(input())
  data.append(d)


for y in range(len(data)):
  for x in range(len(data[0])):
    if data[y][x] == "s":
      sx = x + 1
      sy = y + 1

for y in range(len(data)):
  for x in range(len(data[0])):
    if data[y][x] == "g":
      gx = x + 1
      gy = y + 1
    

data = surround(data)

if dfs(sx, sy) == True:
  print("Yes")
else:
  print("No")




  



