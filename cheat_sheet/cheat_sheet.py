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

s = deque([])

# stack
s.append(1)
s.append(2)
s.append(3)
s.pop()
s.pop()
s.pop()

# queue
q = deque([])
q.append(1)
q.append(2)
q.append(3)
q.popleft()
q.popleft()
q.popleft()

# 2-1-1 部分和問題
def dfs(i, sum):
    





