import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
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

N, M = MAP()
AB = [LIST() for i in range(M)]
K = INT()
CD = [LIST() for i in range(K)]

import itertools
L = [0, 1] #生成する数字
num = K #生成するビット数
bit_list = list(itertools.product([0, 1], repeat=num))

ans = 0
for l in bit_list:
    cnt = 0
    box = [0] * N
    # print(l)
    # print(CD)
    for i, y in enumerate(l):
        # print(i, y, CD[i])
        box_num = CD[i][y] - 1
        box[box_num] += 1
    for a, b in AB:
        if box[a-1] > 0 and box[b-1] > 0:
            cnt += 1
    ans = max(cnt, ans)
print(ans)        
        