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

N, T = MAP()
A = []
B = []
L = [LIST() for i in range(N)]

# 1からi番目の料理で，j分以内に完食できるおいしさの合計の最大値
# dp1[i][j]
dp1 = [[0] * (T) for i in range(N+1)]
# # iからN番目の料理で，j分以内に完食できるおいしさの合計の最大値
# # dp2[i][j]
# dp2 = [[0] * (T) for i in range(N+1)]
# print(L)
# 昇順にする
L.sort()
for a, b in L:
    A.append(a)
    B.append(b)

for i in range(N):
    for j in range(T):
        if j - A[i] >= 0:
            dp1[i+1][j] = max(dp1[i][j-A[i]] + B[i], dp1[i+1][j])
        dp1[i+1][j] = max(dp1[i][j], dp1[i+1][j])

ans = 0
# 最後に一番時間のかかるものをT-1秒目に食べればいい
for k in range(1, N+1):
    ans = max(dp1[k-1][T-1] + B[k-1], ans)
print(ans)




exit()
for i in range(N):
    for j in range(T):
        if j - A[i] >= 0:
            dp1[i+1][j] = max(dp1[i][j-A[i]] + B[i], dp1[i+1][j])
        dp1[i+1][j] = max(dp1[i][j], dp1[i+1][j])
# やりやすく
L = L[::-1]
for i in range(N):
    for j in range(T):
        if j - A[i] >= 0:
            dp2[i+1][j] = max(dp2[i][j-A[i]] + B[i], dp2[i+1][j])
        dp2[i+1][j] = max(dp2[i][j], dp2[i+1][j])
# 戻す
L = L[::-1]
print(L)
ans = 0
for i in range(1, N+1):
    tmp = 0
    for j in range(T):
        tmp = max(tmp, dp1[i-1][j] + dp1[N-i][T-1-j])
    ans = max(ans, tmp+L[i-1][1])
print(ans)