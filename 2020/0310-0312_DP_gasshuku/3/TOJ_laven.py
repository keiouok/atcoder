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

s1 = input()
s2 = input()

dp = [[INF] * (len(s2)+1) for i in range(len(s1)+1)]
dp[0][0] = 0



for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            dp[i+1][j+1] = min(dp[i][j], dp[i][j+1]+1, dp[i+1][j]+1)
        else:
            dp[i+1][j+1] = min(dp[i][j]+1, dp[i][j+1]+1, dp[i+1][j] + 1)

print(dp[len(s1)][len(s2)])
