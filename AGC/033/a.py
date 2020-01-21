import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

h, w = MAP()
A = [list(input()) for i in range(h)]


def bfs():
    que = deque([])
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    d = [[INF] * w for i in range(h)]
    
    for i in range(h):
        for j in range(w):
            if A[i][j] == "#":
                sy, sx = i, j
                d[sy][sx] = 0
                que.append((sy, sx))
    ans = 0
    while que:
        p = que.popleft()
        for i in range(4):
            ny, nx = p[0] + dy[i], p[1] + dx[i]
            
            if 0 <= ny < h and 0 <= nx < w and d[ny][nx] == INF and A[ny][nx] == ".":
                d[ny][nx] = d[p[0]][p[1]] + 1
                # A[ny][nx] = "#"
                que.append((ny, nx))
 
                ans = max(ans, d[ny][nx])     
#    print(*d, sep="\n")
    return ans


if __name__ == "__main__":
    print(bfs())

    

