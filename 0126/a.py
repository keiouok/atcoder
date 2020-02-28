# No DP No LIFE
# 配るDP, 要復習
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
    H, N = MAP()
    L = [LIST() for i in range(N)]
    A = []
    B = []
    for i in range(N):
        A.append(L[i][0])
        B.append(L[i][1])

    dp = [INF] * 20010
    dp[0] = 0
    for i in range(10010):
        for j in range(N):
            dp[i+A[j]] = min(dp[i+A[j]], dp[i]+B[j])
    ans = INF
    for i in range(H, 20010):
        ans = min(ans, dp[i])
    print(ans)

if __name__ == "__main__":
    main()