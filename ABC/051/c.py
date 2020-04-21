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

sx, sy, tx, ty = MAP()

W = tx - sx
H = ty - sy

# first_cicle
A = "U" * H + "R" * W + "D" * H + "L" * W
B = "L" + "U" * (H + 1) + "R" * (W + 1) + "D" \
    + "R" + "D" * (H + 1) + "L" * (W + 1) + "U"
print(A+B)
