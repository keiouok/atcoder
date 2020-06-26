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
A = [input() for i in range(N)]

# alpha_matrix = [[0] * 26 for i in range(26)]
alpha_matrix = []
ans_list = ["no" for i in range(N)]
for i in range(N):
    c = Counter(A[i])
    d = Counter(A[N-i-1])
    for k, v in c.items():
        if d[k] > 0:
            ans_list[i] = k
            ans_list[N-i-1] = k
if "no" in ans_list:
    print(-1)
else:
    print("".join(ans_list))


