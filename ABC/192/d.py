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

def solve(n):
    # num = n進法で表したX
    # num <= M かどうかを返す
    # グローバル変数として定義する
    global X, M
    base = 1
    num = 0
    for x in X:
        num += x * base
        if num > M:
            # 超えた地点で終了
            return False
        base *= n
    return True

# 構造理解
X = list(map(int, list(input())))
X.reverse() # 桁とindexを一致
M = INT()
d = max(X)

if len(X) == 1:
    print(1 if d <= M else 0)
    exit()

ok = 0
ng = pow(10, 18) + 1
# 右端は10 ** 18でいいのだ

# 型を覚えよ
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if solve(mid):
        ok = mid
    else:
        ng = mid
print(max(0, ok - d))
