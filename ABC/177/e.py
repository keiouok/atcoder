import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
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
def divisor(n): #nの約数を全て求める
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table
## 素因数分解
#nを素因数分解したリストを返す
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

N = INT()
A = LIST()
flag = True
A.sort(reverse=True)

memo = defaultdict(int)
s = set()
for a in A:
    d = set(prime_decomposition(a))
    # print(d)
    s = s.union(set(d))
    for y in d:
        if y == 1:
            continue
        elif memo[y] == 0:
            memo[y] += 1
        else:
            # print(d)
            flag = False
# exit()
# print(s)
# exit()
# for a in A:
#     d = divisor(a)
#     set(d)
#     diff = s - set(d)
# for i in range(len(A) - 1):
# A[i]
# cnt = 0
# for a in A:
#     d = divisor(a)
#     # print(d)
#     for y in d:
#         if y == 1:
#             continue
#         if memo[y] == 1:
#             continue
#         else:
#             # print("d:", d)
#             cnt += 1
# if cnt == 0:
#     flag = True
    
if flag == True:
    print("pairwise coprime")
elif reduce(gcd, A) == 1:
        print("setwise coprime")
else:
    print("not coprime")
    

    # A.sort()



