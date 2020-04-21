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
B = [INT() for i in range(N-1)]

tree = defaultdict(list)

for i, b in enumerate(B):
    tree[b-1].append(i+1)

print(tree)
def f(n):
    if not tree[n]:
        return 1
    else:
        f_list = [f(x) for x in tree[n]]
        print(f_list)
        return max(f_list) + min(f_list) + 1

print(f(0))