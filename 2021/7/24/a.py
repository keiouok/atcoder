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
ref = "chokudai"

dic = defaultdict(list)

for i, s in enumerate(S):
    dic[s].append(i)

# search leftest

A = []
for r in ref:
    print(dic[r])
    l = dic[r]
    if r == "c":
        leftest = l[0]
        pr = r
        A.append(leftest)
    else:
        index = bisect(l, leftest)
        if leftest < l[index]:
            leftest = l[index]
            A.append(leftest)

print(A)
q = deque(S)

while q:
    a = q.popleft()
    

