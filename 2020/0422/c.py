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

A = deque(list(input()))
B = deque(list(input()))
C = deque(list(input()))

who = "a"
while 1:
    if who == "a":
        if not A:
            print("A")
            exit()
        who = A.popleft()
    elif who == "b":
        if not B:
            print("B")
            exit()
        who = B.popleft()
    elif who == "c":
        if not C:
            print("C")
            exit()

        who = C.popleft()


    




