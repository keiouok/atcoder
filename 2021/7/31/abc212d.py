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
def S_LIST(): return list(map(str, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

Q = INT()
L = [LIST() for i in range(Q)]

import heapq

total = 0

pq = []
heapq.heapify(pq)

for q in L:
    if q[0] == 1:
        x = q[1]
        heappush(pq, x - total)
    elif q[0] == 2:
        x = q[1]
        total += x   
    elif q[0] == 3:
        x = heappop(pq)
        print(x + total)

