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

N, M, X, Y = MAP()
L = [LIST() for i in range(M)]

dic = defaultdict(list)

# time = 0
for a, b, t, k in L:
    dic[a-1].append([b-1, t, k])
    dic[b-1].append([a-1, t, k])
# print(dic)

visited = [False] * N
# children = q.popleft()
cx = X - 1
# q = deque([dic[cx]])
q = deque([cx])

dist = [INF] * N
time = [INF] * N

start = 0
time[cx] = 0
visited[cx] = True

# print(q)
while q:
    cx = q.popleft()
    children = dic[cx]
    for child in children:
        nx, nt, nk = child
        # print(nx, nt, nk)
        # if visited[nx] == False:
            # visited[nx] = True
        # time[nx]
        # 更新
        if time[cx] % nk != 0:
            plus_time = nk - (time[cx] % nk)
        else:
            plus_time = 0
        # print(time[cx], nk, (time[cx] % nk))
        # print("p:", plus_time)
        if time[cx] + plus_time + nt < time[nx]:
            time[nx] = time[cx] + plus_time + nt
            q.append(nx)
    # print(q)       

# print(time)
if time[Y-1] == INF:
    print(-1)
else:
    print(time[Y-1])
