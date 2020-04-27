import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from heapq import heapify, heappop, heappush
 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, M = MAP()
L = [LIST() for i in range(N)]

# L = [-1, 1] #生成する数字
num = 3 #生成するビット数
bit_list = list(product([-1, 1], repeat=num))

# print(bit_list)
ans = 0
for a, b, c in bit_list:
    tmp = [a * x + b * y + c * z for x, y, z in L]
    tmp.sort(reverse=True)
    selected = sum(tmp[0:M])
    if ans < selected:
        ans = selected
    # ans.append(sum(tmp[0:M]))
print(ans)


