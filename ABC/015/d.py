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

def main():
    W = INT()
    N, K = MAP()
    L = [LIST() for i in range(N)]

    # dp = [K][W][N]
    dp = [[[0] * (N+1) for i in range(W+1)] for i in range(K+1)]
    dp[0][0][0] = 0

    for i in range(1, K+1):
        for j in range(1, W+1):
            for k in range(1, N+1):
                a = L[k-1][0]
                b = L[k-1][1]
                if j-a >= 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-a][k-1]+b)
                dp[i][j][k] = max(dp[i][j][k], dp[i][j][k-1])
    print(dp[K][W][N])
if __name__ == "__main__":
    main()