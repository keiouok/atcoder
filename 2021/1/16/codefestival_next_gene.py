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

S = input()

S = S.split()
ans = set()
B = set()
for s in S:
    i = 0
    while i < len(s):
        b = ""
        if s[i] == "@":
            i += 1
            while i < len(s):
                if s[i] == "@":
                    break
                b += s[i]
                i += 1
            if b.find("0123456789") == -1 and len(b) != 0:
                B.add(b)
        else:
            i += 1
B = list(B)
B.sort()
print(*B, sep="\n")
