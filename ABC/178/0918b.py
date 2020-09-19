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

ans_list = []
while 1:
    N = INT()
    if N == 0:
        break
    L = LIST()
    C = [10, 50, 100, 500]
    for i in range():
        for j in range():
            for k in range():
                for 
    total = 0
    for i in range(4):
        total += L[i] * C[i]
    # for i in range(3, -1, -1):
        a = N % (L[i] * C[i])
    # print(total)
    # a = total - N
    # print("a:", a)
    ans_list.append(total)
    
print(ans_list)

