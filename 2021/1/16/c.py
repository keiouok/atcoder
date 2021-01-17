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
def S_LIST(): return list(map(str, input().split()))

def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 998244353

H, W, K = MAP()
L = [S_LIST() for i in range(K)]

Map = [["N"] * W for _ in range(H)]

for h, w, c in L:
    Map[int(h)-1][int(w)-1] = c
# print(*Map, sep="\n")
dist = [[INF] * W for i in range(H)]

q = deque([(0, 0)])

dh = [0, 1]
dw = [1, 0]

while q:
    ch, cw = q.popleft()
    if Map[ch][cw] == "R":
        for i in range(2):
            nh = ch + dw[i]
            nw = cw
    elif Map[ch][cw] == "D":
        for i in range(2):
            nh = ch + dh[i]
            nw = cw
    # elif Map[ch][cw] == "":
    else:





