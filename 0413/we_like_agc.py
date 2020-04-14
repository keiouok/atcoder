import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from heapq import heapify, heappop, heappush

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()

def no_agc(last4):
    for i in range(4):
        cp_last4 = list(last4)
        if i >= 1:
            cp_last4[i-1], cp_last4[i] = cp_last4[i], cp_last4[i-1]
        cp_last_sent = "".join(cp_last4)
        if cp_last_sent.count("AGC") >= 1:
            return False
    return True

ans = 0
memo = [{} for i in range(N+1)]
def dfs(idx, last3):
    if last3 in memo[idx]:
        print(memo[idx], last3)
        return memo[idx][last3]
    if idx == N:
        return 1
    ret = 0
    for c in "AGCT":
        if no_agc(last3 + c):
            ret = (ret + dfs(idx + 1, (last3 + c)[1:])) % mod
    memo[idx][last3] = ret
    return ret

print(dfs(0, "TTT"))
