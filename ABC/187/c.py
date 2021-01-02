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
S = [input() for i in range(N)]

dict_exist = defaultdict(int)
dict = defaultdict(int)

for s in S:
    if s[0] == "!":
        moji = s[1:]
        if dict[moji] == 1:
            print(moji)
            exit()
        else:
            dict_exist[moji] = 1
    else:
        moji = s
        if dict_exist[moji] == 1:
            print(moji)
            exit()
        else:
            dict[moji] = 1
print("satisfiable")