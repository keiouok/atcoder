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

def divisor(n): #nの約数を全て求める
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

d = divisor(N)
# print(len(d))
# print(sorted(d, reverse=True))
if N == 1:
    print(2)
    exit()
if N % 2 == 0:
    cnt = 0
    for y in d:
        if y % 2 != 0:
            cnt += 1
    print(cnt * 2)
else:
    cnt = 0
    for y in d:
        if y % 2 != 0:
            cnt += 1
    print(cnt * 2)
# else:
#     # print(3)
#     print(4)
