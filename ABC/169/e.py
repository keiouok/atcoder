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

N = INT()
L = [LIST() for i in range(N)]

L.sort(key=lambda x: x[1], reverse=True)
print(L)

l = []


for i in range(N-1):
    a, b = L[i][0], L[i][1]
    c, d = L[i+1][0], L[i+1][1]

    if a <= d <= b:
        if a <= c <= b:
            zone_seki = d - c + 1
            zone_except = b - c
        else:
            zone_seki = d - a + 1
            zone_except = b - c + d - a
        # zone = (d - a + 1)
        # print(zone)
    else:
        diff1 = b - a
        diff2 = d - c
        not_mirror = abs(diff1 - diff2)
        print(not_mirror)
    # ans += not_mirror * 
    



    


