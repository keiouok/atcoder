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

# 17:27 - 18:09
S = input()

c_dic = {c:0 for i, c in enumerate(list("abcdefghijklmnopqrstuvwxyz"))}
origin = "abcdefghijklmnopqrstuvwxyz"

for c in S:
    c_dic[c] += 1

for k, v in c_dic.items():
    # print(k, v)
    if v == 0:
        print(S + k)
        exit()

# len = 26 ver
for i in range(25, 0, -1):
    if S[i-1] < S[i]:
        # wzyxなら，S[i] = z, S[i-1] = wで切れる
        for c in sorted(S[i:]):
            # 切れた右側部分のうち，小さいものからみていく
            # zyx -> xyz
            if c > S[i-1]: # 左側部分で最後のwより大きいcをとる．まずc=x
                print(S[:i-1] + c) # wをcに置き換え左側部分を作成
                exit()
print(-1)                
