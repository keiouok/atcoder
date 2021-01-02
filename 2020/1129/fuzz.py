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
def LIST(): return list(map(float, input().split()))
def S_LIST(): return list(map(str, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

s = input()
L = []
ans = ""
S = s.split(" ")

m = int(S.pop())

L = []
for y in S:
    num, st = y.split(":")
    num = int(num)
    if m % num == 0:
        # ans += st
        L.append([num, st])
L = sorted(L, key=lambda x: x[0])
# print(L)
for num, st in L:
    ans += st
if ans == "":
    print(m)
else:
    print(ans)
