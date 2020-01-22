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


def length(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    return sqrt((x1-x2) ** 2 + (y1-y2) ** 2)


def main():
    N = INT()
    P = []
    num = [n for n in range(N)]
    comb = list(combinations(num, 2))
    for i in range(N):
        P.append(LIST())
    ans = 0
    for c in comb:
        a = P[c[0]]
        b = P[c[1]]
        ret = length(a, b)
        ans = max(ans, ret)
    print(ans)

if __name__ == "__main__":
    main()





