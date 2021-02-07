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

H, W = MAP()
S = [input() for i in range(H)]

M = [[0] * W for i in range(H)]
L = []

for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            M[h][w] = 1

# print(*M, sep="\n")
# Left = []
# Right = []
for h in range(H):
    w = 0
    l = []
    while w < W:
        if M[h][w] == 1:
            left = w
            w += 1
            while M[h][w] == 1:
                w += 1
            right = w
            l.append([left, right])
        w += 1
    if len(l) != 0:
        L.append(l)
# print(L)

# ans = [0] * 4
ans = 0
kaku = 0
cnt = 0
for h in range(len(L)):
    if h == 0:
        for l in L[h]:
            kaku += 2 # ok
    else:
        for l in L[h]:
            left_down, right_down = l
            for lu in L[h-1]:
                left_up, right_up = lu
                if left_down == left_up and right_down == right_up:
                    continue
                elif left_down == left_up: # 左だけ角なし
                    c = 0
                    for l in L[h]:
                        pre_left, pre_right = l
                        c += 1
                        if pre_right < left_down:
                            kaku +=  c * 2
                            break                           
                        if pre_right == left_down:
                            kaku += c * 2 - 2
                            break    
                    # kaku += 2
                elif right_down == right_up:
                    c = 0
                    for l in L[h]:
                        pre_left, pre_right = l
                        c += 1
                        if pre_left > right_down:
                            kaku +=  c * 2
                            break                           
                        if pre_left == right_down:
                            kaku += c * 2 - 2
                            break    

                    # kaku += 2

                elif left_down == left_up: # 左だけ角なし
                    kaku += 2
                elif right_down == right_up:
                    kaku += 2


kaku += len(L[-1]) * 2 # ok
print(kaku)
