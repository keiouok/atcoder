# なぜかうまくいかない
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

N, K = MAP()
R, S, P = MAP()
T = input()
point = {"r": R, "s": S, "p": P}
win = {"r": "p", "s": "r", "p":"s"}

# Tに対して勝つ
win_T = [win[x] for x in T]

ans = 0
for i in range(N):
    if i < K:
        ans += point[win_T[i]]
    # 同じにしたら勝けどできないから変える
    elif win_T[i-K] == win_T[i]:
        win_T[i] = None
    else:
        ans += point[win_T[i]]
print(ans)


