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
X = INT()

# #nを素因数分解したリストを返す
# def prime_decomposition(n):
#   i = 2
#   table = []
#   while i * i <= n:
#     while n % i == 0:
#       n /= i
#       table.append(i)
#     i += 1
#   if n > 1:
#     table.append(n)
#   return table
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

for a in range(-200, 200):
    for b in range(-200, 200):
        if a ** 5 - b ** 5 == X:
            print(a, b)
            exit()
        








# for d in D:
#     ab = d
#     Z = ab // d
#     print(ab, Z)
#     # print((X ** (1/5)))
#     for b in range(int(sqrt(X)) + 1):
#         a = ab - b
#         if a**5-b**5 == X:
#             print("a, b:", a, b)



# for d in divisor(X):
#     ab = d
#     z = X // d
#     for a in range(10 ** 9):
#         b = a - d
#         dot = 
    # for b in range():
    