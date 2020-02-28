import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
A = LIST()

taste = [0] * (10 ** 5 + 1)
left = 0
ans = 0
# if N == 1:
#     print(1)
#     exit()
for right in range(N):
    # まだその味がなければ
    if taste[A[right]] == 0:
        taste[A[right]] = 1
    elif taste[A[left]] == 1:

        while 1:
            # かぶったら
            # if left == right:
            #     right += 1
            if A[left] == A[right]:
                # このまま
                taste[A[right]] = 1
                left += 1
                break
            else:
                # その登録は消して次のleftに更新
                taste[A[left]] = 0
                left += 1
    length = right - left + 1
    ans = max(ans, length)

    # print(right, left, ans)
print(ans)
