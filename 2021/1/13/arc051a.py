import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
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

x1, y1, r = MAP()
x2, y2, x3, y3 = MAP()

import numpy as np

def dist(p1, p2):
    return np.linalg.norm(np.array(p1)-np.array(p2))    

c = (x1, y1)
p1 = (x2, y2)
p2 = (x2, y3)
p3 = (x3, y2)
p4 = (x3, y3)

if x2 <= x1 - r and x1 + r <= x3 and y2 <= y1 - r and y1 + r <= y3:
    print("NO")
    print("YES")
elif max([dist(c, p1), dist(c, p2), dist(c, p3), dist(c, p4)]) <= r:
    print("YES")
    print("NO")
else:
    print("YES")
    print("YES")