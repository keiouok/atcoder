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
A = [INT() for i in range(N)]
ans = [INF] * N

dic = defaultdict(list)
for i, a in enumerate(A):
    dic[a].append(i)

dic = sorted(dic.items(), key=lambda x: x[0])
i = 0
for key, l in dic:   
    for y in l:
        ans[y] = i
    i += 1
print(*ans, sep="\n")
    
