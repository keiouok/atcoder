import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left, bisect_right

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

txa, tya, txb, tyb, t, v = MAP()
N = INT()
L = [LIST() for i in range(N)]
for x, y in L:
    a = sqrt((txa - x) ** 2 + (tya - y) ** 2)
    b = sqrt((txb - x) ** 2 + (tyb - y) ** 2)
    s = a + b
    if s <= t * v:
        print("YES")
        exit()
print("NO")
    

