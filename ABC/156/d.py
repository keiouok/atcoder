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

n, a, b = MAP()

# def c(n,k): 
#   return 1 if(k<=0 or n<=k) else ( c(n-1, k-1) + c(n-1, k) ) %4

# def make_comb_dp(n):
#     dp = [[0] * (n + 1) for i in range(n + 1)]
#     for i in range(n + 1):
#         dp[i][0] = 1
#         dp[i][i] = 1
#     for i in range(2, n + 1):
#         for j in range(1, i):
#             dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
#     return dp





# def c(n,k): 
#   return 1 if(k<=0 or n<=k) else c(n-1, k-1) + c(n-1, k)

# for i in range(10):
#   print([c(i,j) for j in range(i+1)])


MAX = 510000
fac = [0] * MAX
finv = [0] * MAX
inv = [0] * MAX

# // テーブルを作る前処理
MOD = mod
# def COMinit():
#     fac[0] = 1
#     fac[1] = 1
#     finv[0] = 1
#     finv[1] = 1
#     inv[1] = 1
#     # for (i = 2; i < MAX; i++){
#     for i in range(2, MAX):
#         fac[i] = fac[i - 1] * i % MOD
#         inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD
#         finv[i] = finv[i - 1] * inv[i] % MOD
# print(fac)

# // 二項係数計算
def C(n, k):
    if (n < k):
        return 0
    if (n < 0 or k < 0):
        return 0
    else:
        # print(1)
        return fac[n] * (finv[k] * finv[n - k] % mod) % mod

# COMinit()

def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)
# def modinv(a, m):
#     g, x, y = egcd(a, m)
#     if g != 1:
#         raise Exception('modular inverse does not exist')
#     else:
#         return x % m

def combination(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res

c = combination(n, a)
d = combination(n, b)
ans = (2 ** n - c - d -1) % mod
print(ans)






# exit()

# P = [0] * (n + 1)
# P[0]=1
# P[1]=1
#     # // 1を-1にすれば、差分のパスカル三角形になります。
# SIZE = n
# # for y=2;y<SIZE;y++
# for y in range(2, SIZE):
#     b=0
#     # for (r=y;r>0;r--:
#     for r in range(y, 0, -1):
#         P[r]=P[r-1]+b
#         b=P[r-1]
# print(P)


# exit()
# c = [[0] * (n+1) for i in range(n+1)]
# c[0][0] = 1
# for i in range(n):
#     for j in range(n):
#         tmp = c[i][j] % mod
#         c[i+1][j] += tmp
#         c[i+1][j+1] += tmp
# # print()
# # dp = make_comb_dp(n)
# # print(dp)
# print(c)
# soko = (sum(c[n]))
# # print(soko)
# ans = soko - 1 - c[n][a] - c[n][b]
# print(ans % mod)









# # def c(n,k): 
# #   return 1 if(k<=0 or n<=k) else c(n-1, k-1) + c(n-1, k)

# # for i in range(10):
# #   print([c(i,j) for j in range(i+1)])


# # MAX = 510000
# # fac = [0] * MAX
# # finv = [0] * MAX
# # inv = [0] * MAX

# # # // テーブルを作る前処理
# # MOD = mod
# # def COMinit():
# #     fac[0] = fac[1] = 1
# #     finv[0] = finv[1] = 1
# #     inv[1] = 1
# #     # for (i = 2; i < MAX; i++){
# #     for i in range(2, MAX):
# #         fac[i] = fac[i - 1] * i % MOD;
# #         inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD;
# #         finv[i] = finv[i - 1] * inv[i] % MOD

# # # // 二項係数計算
# # def C(n, k):
# #     if (n < k):
# #         return 0
# #     if (n < 0 or k < 0):
# #         return 0
# #     else:
# #         print(1)
# #         return fac[n] * (finv[k] * finv[n - k] % mod) % mod
# # print(C(173205, 141421))

