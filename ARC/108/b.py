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
S = input()
L = []
tmp = len(S)
q = deque([(S, 0)])

# for i in range(N - 2):
i = 0
cnt = 0
while len(S) > i:

    a = S[i:i+3]
    # print("a:", a)
    # if 0 <= i and i + 3 < len(S)
    if a == "fox":
        # j = i
        cnt += 1
        S = S[:i] + S[i+3:]
        # print(S)
        # print(i)
        i -= 2
    else:
        i += 1
# print(S)
print(len(S))

