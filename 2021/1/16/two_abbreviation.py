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
from math import gcd

N, M = MAP()
S = input()
T = input()

def many_lcm(l):
    tmp = l[0]
    for i in range(1, len(l)):
        tmp = tmp * l[i]//gcd(tmp, l[i])
    return tmp

L = many_lcm([N, M])
# print(L)

for i in range(0, N):
    j = i * (L // N)
    print(j)

print("a")
for i in range(0, M):
    j = i * (L // M)
    print(j)

n = N // gcd(N, M)
m = M // gcd(N, M)
g = gcd(N, M)

