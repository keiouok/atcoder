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
A = [list(input()) for i in range(N)]
B = []
wa = set(A[0])
for a in A:
    a.sort()
    # B.append(a)
    wa = set(a) & wa
# print(wa)
dic = defaultdict(int)
for k in wa:
    dic[k] = INF
for k in wa:
    for a in A:
        a.count(k)
        dic[k] = min(dic[k], a.count(k))

dic = sorted(dic.items(), key=lambda x: x[0])
ans = ""
for d in dic:
    ans += d[0] * d[1]
print(ans)


