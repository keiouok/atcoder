import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
import numpy as np
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

H, W, K = MAP()
c = [list(input()) for _ in range(H)]
S = [[0] * W for i in range(H)]
for i in range(H):
    for j in range(W):
        if c[i][j] == "#":
            S[i][j] = 1
S = np.array(S, dtype=np.int32)

ans = 0

for y in product([0, 1], repeat=H):
    for x in product([0, 1], repeat=W):
        Y = [i for i, n in enumerate(y) if n]
        X = [i for i, n in enumerate(x) if n]
        mask = np.zeros((H, W))
        mask[np.ix_(Y, X)] = 1
        ans += np.sum(mask * S) == K
print(ans)

a_2d = np.arange(12).reshape((3, 4))

