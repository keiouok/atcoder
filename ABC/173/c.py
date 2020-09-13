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
import numpy as np
mod = 10 ** 9 + 7
H, W, K = MAP()
L = [input() for i in range(H)]
S = [[0] * W for i in range(H)]
for i in range(H):
    for j in range(W):
        if L[i][j] == "#":
            S[i][j] = 1
S_n = np.array(S)

import itertools
L = [0, 1] #生成する数字


h_b = list(itertools.product([0, 1], repeat=H))
w_b = list(itertools.product([0, 1], repeat=W))


mask = [[0] * W for i in range(H)]

cnt = 0

for h_t in h_b:
    for w_t in w_b:
        for i, h_ in enumerate(h_t):
            for j, w_ in enumerate(w_t):
                mask[i][j] = h_ * w_
        m_n = np.array(mask)
        ada = np.sum(m_n * S_n)
        if ada == K:
            cnt += 1
print(cnt)        
                