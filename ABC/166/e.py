import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, bisect_right
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
A = LIST()

dic = defaultdict(list)
for i, a in enumerate(A):
    dic[a].append(i)
cnt = 0
for i in range(N):
    a = A[i]
    for k, l in dic.items():
        # k + a がimaのiとl[*]の差と等しくなればいい
        tmp = i - (k + a)
        if tmp > 0:
            print(bisect_right(l, tmp))
            if bisect_right(l, tmp) != 0:
                cnt += 1
        # if bisect_left(l, tmp)
            # print("k", k, a)
            # print("l", l)
            # cnt += 1
print(cnt)
        