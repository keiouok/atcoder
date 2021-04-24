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

N, K = MAP()
P = LIST()

a = sum(P[0:K])
ans = a
q = deque(P[0:K])
ans = q
ex = 0
for x in q:
    ex += 1 / 2 * x * (x + 1) / x

pre = ex
for i in range(N - K + 1):
    # print(P[i])
    if i == 0:
        continue
    else:
        # q.popleft()
        # q.append(P[i+K-1])
        # if sum(ans) < sum(q):

        # a = a - P[i-1] + P[i+K-1]
        left = 1/2 *  P[i-1] * (P[i-1] + 1) / P[i-1] 
        right = 1/2 *  P[i+K-1] * (P[i+K-1] + 1) / P[i+K-1] 
        after = pre - left + right
        ex = max(ex, after)
        pre = after
        # if sum(ans) < sum(q):
            # ans = q
        # print(a)
        # c = i
        # a = a + P[c+K] - P[c-1]
        
        # ans = max(a, ans)
        # if ans < tmp:
        #     a = tmp
# print(ans)
# print((1/2 * ans * (ans + 1)) / ans)

print(ex)
# print(ans)
# cnt = 0
# for x in ans:
#     cnt += 1/2 * x * (x + 1) / x
# print(cnt)