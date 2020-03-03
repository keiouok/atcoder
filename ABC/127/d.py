import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
import heapq

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
A = LIST()
L = [LIST() for i in range(M)]
L = sorted(L, key=lambda x : x[1], reverse=True)
default_sum = sum(A)

heapq.heapify(A)  # リストを優先度付きキューへ

for max_cnt, target in L:
    cnt = 0
    while cnt < max_cnt and len(A) != 0:
        min_num = heapq.heappop(A) # pop min
        default_sum += max(target - min_num, 0)
        cnt += 1
    
print(default_sum)



    

exit()
print(heapq.heappop(a))  # 最小値の取り出し

heapq.heappush(a, -2)  # 要素の挿入
print(a)
for i in range(M):
    a = heapq.heappop(A) * (-1)
    a = a // 2
    heapq.heappush(A, -a)
A = list(map(lambda x: x * (-1), A))
print(sum(A))


