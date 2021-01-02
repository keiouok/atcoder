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
cnt = 0
i = 0
memo = [0] * (1 + N)
i = 0
cnt = 0
for i in range(1, N+1):
    if "7" not in str(i):
        if "7" not in str(oct(i)):
            cnt += 1
print(cnt)

exit()

# print((N + 1) // 8)
# print((N + 1) // 8)




# exit()
# while 10 * i + 7 <= N :
#     a = 10 * i + 7
#     memo[a] = 1
#     i += 1

# i = 0
# while 8 * i + 7 <= N:
#     a = 8 * i + 7
#     memo[a] = 1
#     i += 1
# print(N - sum(memo))



# # exit()
# # for i in range(1, N+1):
# #     if i % 10 != 7 and i % 8 != 7:
# #         cnt += 1
# # # 8
# # print((N + 1) // 8)
# # # 10
# # print((N + 3) // 10)

# # print(N // 40)

# # print(cnt)