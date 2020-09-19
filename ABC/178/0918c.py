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

ans = []
while 1:
    W, H = MAP()
    if W == 0 and H == 0:
        break
    L = [LIST() for i in range(2 * H - 1)]
    q = deque([()])
    q.append((0, 0))
    visited = [[False] * W for i in range(H)]
    visited[0][0] = True
    dist = [[INF] * W for i in range(H)]
    dist[0][0] = 1
    dw = [1, 0, -1, 0] 
    dh = [0, 1, 0, -1]
    #  1, 3 right left
    #  2, 4 up, down
    while q:
        cw, ch = q.popleft()
        for i in range(4):
            nw = cw + dw[i]
            nh = ch + dh[i]
            # if 0 <= nw < W and 0 <= nh < H:
            #     if visited[nh][nw] == False:
            #         if i == 0:
            #             if L[ch][cw] == 2:
