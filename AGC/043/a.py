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

H, W = MAP()
S = [input() for i in range(H)]
# 1
dp = [[INF] * W for i in range(H)]
dp[0][0] = 0
# 
# if S[0][0] == ".":
#     dp[0][0] = 0
# else:
#     dp[0][0] = 1

# 異なるやつにできるだけ合わなければいい
for h in range(1, H):
    if S[h][0] == S[h-1][0]:
        dp[h][0] = dp[h-1][0]
    else:
        dp[h][0] = dp[h-1][0] + 1
# yoko
# print(dp)
for w in range(1, W):
    if S[0][w] == S[0][w-1]:
        dp[0][w] = dp[0][w-1]
    else:
        dp[0][w] = dp[0][w-1] + 1
# print(*dp, sep="\n")

for i in range(1, H):
    for j in range(1, W):
        # nokori
        if S[i][j] == S[i-1][j] and S[i][j] == S[i][j-1]:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])
        elif S[i][j] != S[i-1][j] and S[i][j] == S[i][j-1]:
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1])
        elif S[i][j] == S[i-1][j] and S[i][j] != S[i][j-1]:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]+1)            
        else:   
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)

# print(*dp, sep="\n")
last = dp[H-1][W-1]
if S[0][0] == S[H-1][W-1] == ".":
    # #.#.の繰り返しがdp[]
    ans = last // 2
elif S[0][0] == S[H-1][W-1] == "#":
    ans = 1 + last // 2

elif S[0][0] != S[H-1][W-1]:
    ans = (last + 1) // 2
print(ans)



        # if S[i][j] == ".":
        #     dp[i][j] = min(dp[i-1][j], dp[i][j-1])
        # else:
        #     dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1




exit()
# print(dp)
# exit()
for i in range(1, H):
    for j in range(1, W):
        # nokori
        if S[i][j] == ".":
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

ans1 = dp[H-1][W-1]
print(dp)
# print(ans1)


# 一回前半+1, ##
S_r = []
for i in range(H):
    l = []
    for j in range(W):
        if S[i][j] == ".":
            l.append("#")
        else:
            l.append(".")
    S_r.append(l)
dp = [[INF] * W for i in range(H)]
S = deepcopy(S_r)
if S[0][0] == ".":
    dp[0][0] = 0
else:
    dp[0][0] = 1

# tate
for h in range(1, H):
    if S[h][0] == "#":
        dp[h][0] = dp[h-1][0] + 1
    else:
        dp[h][0] = dp[h-1][0]
# yoko
for w in range(1, W):
    if S[0][w] == "#":
        dp[0][w] = dp[0][w-1] + 1
    else:
        dp[0][w] = dp[0][w-1]
# exit()
for i in range(1, H):
    for j in range(1, W):
        # nokori
        if S[i][j] == ".":
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

ans2 = dp[H-1][W-1]

print(min(ans1, ans2+1))


exit()

# # 
# dp2 = deepcopy(dp)

# for i in range(1, W):
#     for j in range(1, H):
#         # nokori
#         if S[j][i] == ".":
#             dp2[j][i] = min(dp2[j-1][i], dp2[j][i-1])
#         else:
#             dp2[j][i] = min(dp2[j-1][i], dp2[j][i-1]) + 1
# print("h")
# print(*dp, sep="\n")





# print(dp2)
# print(ans1)


# exit()
# second



dp = [[0] * W for i in range(H)]

# 
if S[0][0] == "#":
    dp[0][0] = 0
else:
    dp[0][0] = 1

# tate
for h in range(1, H):
    if S[h][0] == ".":
        dp[h][0] += dp[h-1][0] + 1
    else:
        dp[h][0] = dp[h-1][0]
# yoko
for w in range(1, W):
    if S[0][w] == ".":
        dp[0][w] += dp[0][w-1] + 1
    else:
        dp[0][w] = dp[0][w-1]
# print(dp)
# exit()
for i in range(1, H):
    for j in range(1, W):
        # nokori
        if S[i][j] == "#":
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

ans2 = dp[H-1][W-1]

print(ans1, ans2)
print(min(ans1, ans2+1))