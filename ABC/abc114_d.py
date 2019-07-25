
import sys, re
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
def LIST(): return list(map(int, input().split()))
# def LIST(): return list(map(str, input().split()))
# def LIST(): return list(input())

sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
e = [0] * (N + 1)
for i in range(2, N + 1):
    cur = i
    for j in range(2, i + 1):
        while cur % j == 0:
            e[j] += 1
            cur //= j
    
def num(m):
    res = len(list(filter()))