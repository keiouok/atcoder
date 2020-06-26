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
A = LIST()
A.sort()

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

dic = defaultdict(int)
no_exist = 0
ans = 0
kaburi = defaultdict(int)
for a in A:
    kaburi[a] += 1

for a in A:
    if kaburi[a] == 1:
        no_exist = 0
        prime = set(prime_decomposition(a))
        print("p", prime)
        for p in prime:
            p = int(p)
            if dic[p] != 0:
                no_exist += 1
            
        if no_exist == 0:
            ans += 1
    dic[a] += 1
print(ans)  
