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

dx = [0, 1, 0, -1]
dy = [1, 0 ,-1, 0]
ans = 0

for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            # 0 is kouho
            q = deque([[h, w]])
            cost = [[0] * W for i in range(H)]
            visited = [[False] * W for i in range(H)]
            while q:
                # print("q:", q.popleft())
                h1, w1 = q.popleft()

                visited[h1][w1] = visited[True]
                for i in range(4):
                    h_next = h1 + dy[i]
                    w_next = w1 + dx[i]
                    if 0 <= h_next < H and 0 <= w_next < W:
                        s_next = S[h_next][w_next]
                        if s_next != S[h1][w1]:
                            if visited[h_next][w_next] == False:
                                visited[h_next][w_next] = True
                                cost[h_next][w_next] += 1
                                q.append([h_next, w_next])
            # print("******")
            # print(*cost, sep="\n")
            for h in range(H):
                for w in range(W):
                    if S[h][w] == "#":
                        ans += cost[h][w]//2
                    else:
                        ans += cost[h][w]      
            # print(ans)
# print(*cost, sep="\n")

# ans = 0
# for h in range(H):
#     for w in range(W):
#         ans += cost[h][w]
print(ans)




