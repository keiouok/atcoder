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

if N <= 9:
    print(N+9)
    exit()

# 和
k = sum(int(c) for c in str(N))
# 商とあまり
d, m = divmod(k-1, 9)
ans = str(m+1) + "9" * d
# 同じなら
if N == int(ans):
    if ans[0] == "9":
        ans = "18" + ans[1:]
    else:
        ans = str(int(ans[:2])+9) + ans[2:]
print(ans)