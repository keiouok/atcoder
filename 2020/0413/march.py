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
S = [input() for i in range(N)]

dic = defaultdict(int)
for s in S:
    if s[0] in "MARCH":
        dic[s[0]] += 1

march = list("MARCH")
comb = list(combinations(march, 3))

ans = 0
for a, b, c in comb:
    ans += dic[a] * dic[b] * dic[c]
print(ans)




