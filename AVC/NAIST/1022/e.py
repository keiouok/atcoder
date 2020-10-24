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

while 1:
    W, H = MAP()
    if W == 0 and H == 0:
        break
    C = [LIST() for i in range(H)]
    visited = [[INF] * W for i in range(H)]
    M = [[0] * W for i in range(H)]
    q = deque([(0, 0)])
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    while q:
        ch, cw = q.popleft()
        if visited[ch][cw] == True:
            continue
        
        for h in range(H):
            for w in range(W):
                # if M[i] == 1:
                if C[h][w] == 1:
                    M[h][w] += 1
                    for i in range(8):
                        nh = h + dy[i]
                        nw = w + dx[i]
                        if 0 <= nh < H and 0 <= nw < W:
                            if C[nh][nw] == 1:
                                M[nh][nw] = M[nh][nw] + 1
                    
    print(*M, sep="\n")



    # while q:
    #     h, w = q.popleft()
    #     if visited[h][w] == False:
    #         if M[h][w] == 
    #         visited[h][w] = True





