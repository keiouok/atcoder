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
pre_S = S
T = input()
s = len(S)
t = len(T)
key = []
for i in range(len(S)-len(T)+1):
    # print(S[i:i+t])
    same = 0
    for j, y in enumerate(S[i:i+t]):
        if y == "?":
            same += 1
            continue
        else:
            if y == T[j]:
                same += 1
    if same == t:
        # print(S[i:i+t])
        key.append(i)
    # print(y)
# l = list(S)
if key:
    ans = "z" * 60
    for i in key:
        # ここ言い換えたらだめ
        S_ = S[:i] + T + S[i+t:]
        tmp = ""
        for i in range(len(S_)):
            if S_[i] == "?":
                tmp += "a"
            else:
                tmp += S_[i]
        ans = min(ans, tmp)
    print(ans)
else:
    print("UNRESTORABLE")

