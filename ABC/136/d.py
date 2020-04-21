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

S = input()
tmp = "R"
index = [0]
ans = [0] * len(S)
for i, s in enumerate(S):
    if tmp != s:
        index.append(i)
        if tmp == "R":
            tmp = "L"
        else:
            tmp = "R"
index.append(len(S))

for i in range(len(index)-1):
    left = index[i]
    right = index[i+1]
    tmp = S[left:right]
    same_num = right - left
    if tmp[0] == "R":
        # rinsetu L
        ans[right] += same_num // 2
        # rinsetu R
        ans[right-1] += ceil(same_num / 2)

    else:#L renzoku
        # L
        ans[left] += ceil(same_num / 2)
        # R
        ans[left-1] += same_num // 2
print(*ans)
