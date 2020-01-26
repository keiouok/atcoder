import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect
 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

def main():
    H, W = MAP()
    S = [input() for i in range(H)]
    # 上下左右
    L = [[0] * W for i in range(H)]
    R = [[0] * W for i in range(H)]
    D = [[0] * W for i in range(H)]
    U = [[0] * W for i in range(H)]
    
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                L[i][j] = 0
            elif j == 0:
                L[i][j] = 1
            else:
                L[i][j] = L[i][j-1] + 1
            
    for i in range(H):
        for j in range(W-1, -1, -1):
            if S[i][j] == "#":
                R[i][j] = 0
            elif j == W-1:
                R[i][j] = 1
            else:
                R[i][j] = R[i][j+1] + 1
    
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                U[i][j] = 0
            elif i == 0:
                U[i][j] = 1
            else:
                U[i][j] = U[i-1][j] + 1

    for i in range(H-1, -1, -1):
        for j in range(W):
            if S[i][j] == "#":
                D[i][j] = 0
            elif i == H-1:
                D[i][j] = 1
            else:
                D[i][j] = D[i+1][j] + 1
    ans = 0
    for i in range(H):
        for j in range(W):
            ans = max(ans, L[i][j] + R[i][j] + U[i][j] + D[i][j] - 3)
    print(ans)

if __name__ == "__main__":
    main()


