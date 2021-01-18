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

S = list(input())
L = LIST()

l = []

S = deque(S)
L = deque(L)
# for i, s in enumerate(S):
i = 0

print(len(S))
while i <= len(S):
    if i == L[0]:
        a = L.popleft()
        l.append("\"")
    if i != len(S):
        l.append(S[i])
    i += 1

print("".join(l))   


