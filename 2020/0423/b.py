import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from heapq import heapify, heappop, heappush
 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

X = INT()
# ans = 0
# for b in range(1, 1000):
#     for p in range(2, 1000):
#         tmp = b ^ p
#         # print(tmp)
#         if tmp <= X:
#             ans = max(ans, tmp)
#             # print(tmp)
#         else:
#             break
# print(ans)
def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table

x = X
r = [1]
for i in range(2, x + 1):
    c = 2
    while i ** c <= x:
        r.append(i ** c)
        c += 1
ans = sorted(r)[-1]
print(ans)


exit()


for x in range(X, 0, -1):
    prime = prime_decomposition(x)
    c = Counter(prime)
    # print(c.values())
    value = c.values()
    # print(v)
    print(c)
    for v in value:
        d = v
    if len(c) == 1 and d >= 2:
        print(x)
        exit()
    elif x == 1:
        print(x)
        exit()
    

