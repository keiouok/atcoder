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

N = INT()
P = LIST()
flag = True
now = 0
x = 1
ans = []
for i in range(N):
    if P[i] == i + 1:
        print(-1)
        exit()
    if P[i] == x:
        P[now:i+1] = [x] + P[now:i]
        for j in range(now, i):
            if P[j] != j + 1:
                print(-1)
                exit()
            else:
                for k in range(i, now, -1):
                    ans.append(k)
                now = i
                x = i + 1
                # 後半の部分でnow(index)と数が同じなら無理
                # now == N - 1ならOK，最後だから同じでOK
                if P[now] == x and now != N - 1:
                    print(-1)
                    exit()
print(*ans, sep="\n")




