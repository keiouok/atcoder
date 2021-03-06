import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
XY = [LIST() for i in range(N)]
L = [i for i in range(N)]
A = list(combinations(L, 3))

def r(x1, x2, y1, y2):
    r = (y2 - y1) / (x2 - x1)
    return r    

for c in A:
    x1, y1 = XY[c[0]]
    x2, y2 = XY[c[1]]
    x3, y3 = XY[c[2]]
    if x1 == x2 == x3:
        print("Yes")
        exit()
    elif y1 == y2 == y3:
        print("Yes")
        exit()
    elif x1 == x2 or x2 == x3 or x3 == x1:
        continue
    else:
        if r(x1, x2, y1, y2) == r(x1, x3, y1, y3):
            print("Yes")
            exit()
print("No")
