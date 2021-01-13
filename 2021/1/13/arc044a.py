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

def is_prime(n):
    for i in range(2, n+1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1

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

N = INT()
# print(divisor(N))
if is_prime(N):
    print("Prime")
    exit()
elif len(divisor(N)) > 2:
    l = list(str(N))
    l = [int(y) for y in l]
    if (N % 10) % 2 != 0 and (N % 10) % 5 != 0 and sum(l) % 3 != 0:
        print("Prime")
        exit()
print("Not Prime")


