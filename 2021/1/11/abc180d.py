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
from decimal import Decimal

# 16:00 - 16:28
X, Y, A, B = MAP()
exp = 0

# XがA倍される，が，XにB足される以下ならばそちらを増やした方が経験値は上がる．
# AtCoder Gymの方が入るpowerが小さいなら，AtCoder Gymの方がいい
while A * X <= X + B and A * X < Y:
    X *= A
    exp += 1

# 残りはAtCoder Gymに任せる
power = Y - 1 - X
# Y以上がダメという点に注意！
exp += power // B
print(exp)