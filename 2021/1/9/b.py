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
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
L = [LIST() for i in range(N)]

dic = defaultdict(list)
i = 0

for a, b in L:
    dic[a].append(i)
    dic[b].append(i)
    i += 1

print(dic)


exit()
dp = [[set()] * 2 for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(2):
        s1 = L[i-1][0]
        s2 = L[i-1][1]
        l1 = dp[i-1][0] | set([s1])
        l2 = dp[i-1][1] | set([s2])
        if len(l1) >= len(l2):
            dp[i][j] = l1
        else:
            dp[i][j] = l2
        # print(l1, l2)
# print(len(dp[N][0])
ans = max(len(dp[N][0]), len(dp[N][1]))
print(ans)