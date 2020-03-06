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
    N, M = MAP()
    dp = [INF] * (1<<N)
    dp[0] = 0

    for i in range(M):
        a, b = MAP()
        c = LIST()
        d = 0
        # 1を立てる
        for x in c:
            # 1が存在するなら，dの一番最後，右から0番目，0シフト目に必要
            d += 1<<(x-1)
        for j in range(1<<N): # 2 ** N 列見る
    #         # テーブルは一列ずつ見て更新しよう
            tmp = j|d
            dp[tmp] = min(dp[tmp], dp[j] + a)
    if dp[-1] == INF:
        print(-1)
    else:
        print(dp[-1])

if __name__ == "__main__":
    main()