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

S, P = MAP()

a = S ** 2 - 4 * P
import math
# a = -1
if a < 0:
    print("No")
    exit()
M1 = (S + math.sqrt(a)) / 2
M2 = (S - math.sqrt(a)) / 2
N1 = S - M1
N2 = S - M2
# print(M1, N1)
# print(M2, N2)
if int(N1) == N1 and int(M1) == M1:
    if N1 > 0 and M1 > 0:
        print("Yes")
        exit()

if int(N2) == N2 and int(M2) == M2:
    if N2 > 0 and M2 > 0:
        print("Yes")
        exit()
print("No")