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

while 1:
    W, H = MAP()
    if W == 0 and H == 0:
        break
    else:
        L = [input() for i in range(H)]
        ans_l = []

# while 1:
#     W, H = MAP()
#     if W == 0 and H == 0:
#         break
#     else:
#         L = [input() for i in range(H)]
#         ans_l = []
#         # def bfs()
#         dx = [1, 0]
#         dy = [0, -1]
#         ma = -1
#         for h in range(H):
#             for w in range(W):
#                 q = deque([h, w])
#                 # visited = []
#                 stock = []
#                 # memo = [[""] * W for i in range(H)]
#                 memo = L
#                 ans = ""
#                 while q:
#                     cy, cx = q.popleft()
#                     cy, cx = int(cy), int(cx)
#                     ans = memo[cy][cx]
#                     if 0 <= int(L[cy][cx]) <= 9:
#                         # moto = L[cy][cx]
#                         for i in range(2):
#                             nx = cx + dx[i]
#                             ny = cy + dy[i]
#                             if 0 <= ny < H and 0 < nx < W and 0 <= int(L[ny][nx]) <= 9:
#                                 if int(memo[cy][cx] + memo[ny][nx]) > int(memo[cy][cx]):
#                                     memo[ny][nx] = memo[cy][cx] + memo[ny][nx]
#                                     ans = memo[ny][nx]
#                                 q.append([ny, nx])
#                 if ans == "":
#                     tmp = -1
#                 else:
#                     tmp = int(ans)
#                 # ans_l.append(ans)
#                 # if ma == -1:
#                 #     print("No")
#                 # else:
#                 #     if ma < tmp:
#                 ans_l.append(tmp)
#             if max(ans_l) == -1:
#                 print("No")
#             else:
#                 print(max(ans_l))