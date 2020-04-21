import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left, bisect_right

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

# last4 の文字列
def no_agc_is(last4):
    for i in range(4):
        t = list(last4)
        if i >= 1:
            # swap
            t[i-1], t[i] = t[i], t[i-1]
        # 4charでできた文字列中にAGCがあればfalse
        if "".join(t).count("AGC") >= 1:
            return False
    return True

# 0, 1, 2, 3
memo = [{} for i in range(N+1)]
# memo[0] = {}
# memo[0] = {"TTT": 4}とか
# memo[1]
def dfs(cur, last3):
    # cur, last3 = q.pop()
    # 同じやつあったらメモした奴呼び出し
    if last3 in memo[cur]:
        return memo[cur][last3]
    if cur == N:
        return 1
    ret = 0
    for c in "ACGT":
        if no_agc_is(last3 + c):
            ret = (ret + dfs(cur + 1, (last3 + c)[1:])) % mod
    memo[cur][last3] = ret
    return ret
print(dfs(0, "TTT"))