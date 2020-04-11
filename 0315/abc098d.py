# なぜかうまくいかない
import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_right, bisect_left

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

e = [0] * (N + 1)

for i in range(2, N + 1):
    cur = i
    for j in range(2, N + 1):
        while cur % j == 0:
            # 割り切れるなら，割り切れるjの数を数える
            e[j] += 1
            cur //= j
def num(m):
    return len(list(filter (lambda x: x >= m - 1, e)))

ans = num(75) + num(25) * (num(3) - 1) + num(15) * (num(5) - 1) + num(5) * (num(5) - 1) * (num(3) - 2) // 2
print(ans)
# for n in range(1, N+1):
#     prime = prime_decomposition(n)
#     print(prime)
#     for p in prime:
#         p = int(p)
#         prime_num[p] += 1
# print(prime_num)
# num = [0] * 81
# for p_num in prime_num:
#     # if p_num <= 80:
#     p_num = min(80, p_num)
#     for i in range(1, p_num+1):
#         num[i] += 1
# print(num)
# # 同じ素数は取らないように
# ans = num[75] + num[25] * (num[3] - 1) + num[15] * (num[5] - 1) + num[5] * (num[5] - 1) * (num[3] - 2) // 2
# print(ans)    
