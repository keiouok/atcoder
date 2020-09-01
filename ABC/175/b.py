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


from itertools import combinations_with_replacement
N = INT()
L = LIST()

C = Counter(L)
S = sorted(set(L))
# print(S)
# print(C)

A = list(combinations(S, 3))
# print(a)
cnt = 0
for a, b, c in A:
    if a != b != c:
        if a + b > c:
            # print(a, b, c)
            # print(c[a])
            # print(c[a])
            cnt += C[a] * C[b] * C[c]
print(cnt)

# cnt = 0
# p = 0
# for idx in range(len(S)-1):
#     p = 0
#     while p + idx != len(S) - 1:
#         s_num = c[S[idx]]
#         min_wa = S[idx] + S[idx + p]
#         print(min_wa)
#         right = S[idx+2:]
#         print(right)
#         a = bisect_left(right, min_wa)
#         print("idx", a)
#         cnt += a * s_num
#         p += 1
# print(cnt)