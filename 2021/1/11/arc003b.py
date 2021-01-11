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

# 12:17 - 12:28
N = INT()
S = [input() for i in range(N)]

L = []
dic = defaultdict(str)
for s in S:
    # dic[s]
    l = list(s)
    # reversed(l)
    l.reverse()
    rs = "".join(l)
    dic[rs] = s
dic = sorted(dic.items(), key=lambda pair: pair[0], reverse=False)
# print(dic)
for k, v in dic:
    print(v)

