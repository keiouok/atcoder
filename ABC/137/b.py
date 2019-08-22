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

k, x = MAP()

l = []


# l.append(x+1)
# l.append(x)
# l.append(x-1)
# for j in range(x):
for i in range(k):
    # print(x-i)
    # print(x+i)
    l.append(x-i)
    l.append(x+i)
    # l.append(x-i)
l.sort()
s = set(l)
l = list(s)
# print(l)
l.sort()
# print(l)
# s = ",".join(l)
# print(s)
s_l = []

for i in l:
    s_l.append(str(i))
    s_l.append(" ")
print("".join(s_l))

# for i in l:
#     print(i)
# s = "".join(l)
# print()
# print(l.join(","))
# for i in range(l)
# print(l)