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

N = INT()
S = input()

b = deque(["b"])

if N % 2 != 1:
    print(-1)
    exit()

x = (N + 1) // 2

for n in range(x):
    if n == 0:
        continue
    elif n % 3 == 1:
        b.appendleft("a")
        b.append("c")
    elif n % 3 == 2:
        b.append("a")
        b.appendleft("c")
    elif n % 3 == 0:
        b.append("b")
        b.appendleft("b")

b = "".join(b)
if b == S:
    print(x-1)
else:
    print(-1)