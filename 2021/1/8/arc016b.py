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

X = [input() for i in range(N)]

cnt = 0
tmp = 0
for w in range(9):
    for j in range(N):
        if X[j][w] == "x":
            cnt += 1
            tmp = 0
        elif X[j][w] == "o":
            if tmp == 0:
                cnt += 1
            # elif tmp == 1:
            #     continue
                tmp = 1
        elif X[j][w] == ".":
            tmp = 0
    tmp = 0

print(cnt)