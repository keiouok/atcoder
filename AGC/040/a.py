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

S = input()
left = 0
right = 0
for i in range(len(S)):
  if S[i] == ">":
    left += 1
  else:
    break
for i in range(len(S)):
  if S[len(S)-i-1] == "<":
    right += 1
  else:
    break
# print(left)
# print(right)

if right != 0:
  S = S[left:-right]
else:
  S = S[left:]

ruiseki = [0] * len(S)
r, l = 0, 0

# for i in range(len(S)):
#   if S[i] == "<":
#     # l += 1
#     ruiseki[i+] = ruiseki[i]
#   elif S[i] == ">":
#     # r += 1
#     ruiseki[i] += 1
# print(ruiseki)

left_box = []
right_box = []
# left
count = 0
for i in range(len(S)):
  if S[i] == "<":
    count += 1
  else:
    if count != 0:
      left_box.append(count)
    count = 0
if count != 0:
  left_box.append(count)
      
# print(left_box)

for i in range(len(S)):
  if S[i] == ">":
    count += 1
  else:
    if count != 0:
      right_box.append(count)
    count = 0
if count != 0:
  right_box.append(count)


# print(right_box)
  
m = []
for i in range(len(right_box)):
  r = right_box[i]
  l = left_box[i]
  m.append(max(r, l))
# print(m)
count = 0

for i in range(len(m)):
  for j in range(1, m[i]+1):
    count += j
# print(count)

# for i in range(len(m))
ans = 0

def wa(num):
  wa = 0
  for i in range(1,num+1):
    wa += i
  return wa

def small_wa(num):
  wa = 0
  for i in range(0, num):
    wa += i
  return wa

for i in range(len(right_box)):
  r = right_box[i]
  l = left_box[i]
  b = max(r, l)
  s = min(r, l)
  a = small_wa(s) + wa(b)
  ans += a
  # print(a)


# nokori
ans += wa(left) + wa(right)
print(ans)


