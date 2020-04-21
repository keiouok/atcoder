import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

R, C, K = MAP()
# S = [INT() for i in range(R)]
S = ["x" * (C + 2)] + \
    ["x" + input() + "x" for i in range(R)] + \
    ["x" * (C + 2)]

q = deque()
cnt = [[0] * (C + 2) for _ in range(R + 2)]

for i in range(R + 2):
    for j in range(C + 2):
        if S[i][j] == "x":
            q.append((i, j))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

while q:
    i, j = q.popleft()
    for k in range(4):
        x = j + dx[k]
        y = i + dy[k]
        if 0 <= x < C + 2 and 0 <= y < R + 2 and S[y][x] != "x" and cnt[y][x] == 0:
            cnt[y][x] = cnt[i][j] + 1
            q.append((y, x))
ans = 0
# print(*cnt, sep="\n")
for i in range(1, R + 1):
    for j in range(1, C + 1):
        if cnt[i][j] >= K:
            ans += 1
print(ans)
