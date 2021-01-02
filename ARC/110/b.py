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

N = INT()
T = input()

a = N // 3
b = N % 3
cnt = 0

if T == "1":
    print(2 * 10 ** 10)
    exit()
elif T == "11":
    print(10 ** 10)
    exit()
for s in ["110", "101", "011"]:
    a = N // 3
    b = N % 3
    if T == a * s + s[:b]:
        cnt += 1

if cnt == 0:
    print(0)
    exit()
    # Tは必ず0を含む
else:
    K = Counter(T)["0"]
    if T[-1] == "0":
        print(10 ** 10 - K + 1)
    elif T[-1] == "1":
        print(10 ** 10 - K)
