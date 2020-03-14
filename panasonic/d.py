import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left, bisect_right

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))

sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

l = 'abcdefghijklmnopqrstuvwxyz'
N = INT()

# ans = (N-1) * "a" + 

# for i in range():
# p1 = "a" * N
q = ["a"]

# def dfs():
    # a = q.pop()
    # while q:
a = "a"
k = [n for n in l[:N]]
# print(k)
# for i in range(N):
# def dfs():
kazu = []
for i in range(1, N):
    y = k[:i]
    u = k[:i+1]
    B = list(product(y, u))
    for b in B:
        # for c in b:
        kazu.append("".join(b))
kazu.sort()
print(*kazu, sep="\n")




    

