import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

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
d1_list = [0] * (N + 1)
d2_list = [0] * (N + 1)
for i in range(2, N + 1):
    print("? {0} {1}".format(1, i))
    sys.stdout.flush()
    dist = INT()
    d1_list[i] = dist

# 一番大きかったもののindex
idx = d1_list.index(max(d1_list))
for i in range(1, N+1):
    if i == idx: continue
    print("? {0} {1}".format(idx, i))
    sys.stdout.flush()
    dist = INT()
    d2_list[i] = dist

print("! {}".format(max(d2_list)))