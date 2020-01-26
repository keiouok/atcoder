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

def gcd(a, b):
# 例外処理
    if a == 0:
        return b
    if b == 0:
        return a

    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b

def main():
    N = INT()
    A = LIST()
    A.insert(0, 0)
    A.append(0)
    L = [0] * (N + 2)
    R = [0] * (N + 2)
    L[0] = 0
    # R[]
    R[N + 1] = 0
    for i in range(0, N + 1):
        L[i + 1] = gcd(L[i], A[i])
    for i in range(N, -1, -1):
        R[i] = gcd(R[i + 1], A[i])

    # print(L)
    # print(R)
    ans = 0
    for i in range(1, N + 1):
        ans = max(ans, gcd(L[i], R[i+1]))
    print(ans)

if __name__ == "__main__":
    main()


