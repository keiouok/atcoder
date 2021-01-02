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
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
A = LIST()

dp = [[[0] * 310 for i in range(310)] for j in range(310)]

dish = Counter(A)
a = dish[1]
b = dish[2]
c = dish[3]

for i in range(1, N+1):
    for j in range(min(i, b + c)+1):
        for k in range(min(j, c)+1):
            res = 0
            if i - j > 0:
                res += dp[i-j-1][j-k][k] * (i - j)
            if j - k > 0:
                res += dp[i-j+1][j-k-1][k] * (j - k)
            if k > 0:
                res += dp[i-j][j-k+1][k-1] * k
            res += N
            res /= (i - j + j - k + k)
            dp[i-j][j-k][k] = res


ans = dp[a][b][c]
# ans = f(a, b, c)
print(ans)
