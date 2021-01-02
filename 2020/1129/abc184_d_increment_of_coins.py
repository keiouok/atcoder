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

a, b, c = MAP()

dp = [[[0] * 101 for i in range(101)] for i in range(101)]

def f(a, b, c):
    if dp[a][b][c]:
        return dp[a][b][c]
    if a == 100 and b == 100 and c == 100:
        return 0
    ans = 0
    ans += f(a + 1, b, c) * a / (a + b + c)
    ans += f(a, b + 1, c) * b / (a + b + c)
    ans += f(a, b, c + 1) * c / (a + b + c)
    dp[a][b][c] = ans
    return ans

# dp[100][*][*] = 0
# dp[*][100][*] = 0
# dp[*][*][100] = 0

for i in range(99, -1, -1):
    for j in range(99, -1, -1):
        for k in range(99, -1, -1):
            if (i + j + k == 0):
                continue
            now = 0
            now += dp[i+1][j][k] * i
            now += dp[i][j+1][k] * j
            now += dp[i][j][k+1] * k
            dp[i][j][k] = now / (i + j + k) + 1
ans = dp[a][b][c]
print(ans)
