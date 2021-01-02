import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(float, input().split()))
def S_LIST(): return list(map(str, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, M = MAP()
visited = [[False] * M for i in range(N)]
Map = [input() for i in range(N)]

q = deque([[N-1, 0]])
print(q)
ans = 0
while q:
    ch, cw = q.popleft()
    print("a:", ch, cw)
    print(Map[ch][cw])
    if Map[ch][cw] == "S":
        print("here")
        nh = ch - 1
        nw = cw
    elif Map[ch][cw] == "E":
        nh = ch
        nw = cw + 1
    elif Map[ch][cw] == "W":
        nh = ch
        nw = cw - 1
    elif Map[ch][cw] == "N":
        nh = ch + 1
        nw = cw
    print(nh, nw)
    if 0 <= nh < N and 0 <= nw < M:
        if visited[nh][nw] == False:
            ans += 1
            q.append([nh, nw])
            print(ans)

print(ans)
