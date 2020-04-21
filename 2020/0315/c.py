# なぜかうまくいかない
import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_right, bisect_left

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

S = S_LIST()
N = INT()
T = [input() for i in range(N)]
ans = []
flag = False
for s in S:
    flag = False
    for t in T:
        if len(s) == len(t):
            if t.count("*") >= 1:
                if t.count("*") == len(t):
                    # ans.append("*" * len(t))
                    # print(t.count("*"))
                    flag = True
                else:
                    num = t.count("*")
                    cnt = 0
                    for i in range(len(t)):
                        if t[i] != "*":
                            if t[i] == s[i]:
                                cnt += 1
                    if num == len(t) - cnt:
                        # ans.append("*" * len(t))
                        flag = True
            else:
                if s == t:
                    # ans.append("*" * len(t))
                    flag = True
                    break
    if flag:
        ans.append("*" * len(s))
    else:
        ans.append(s)
print(*ans)





