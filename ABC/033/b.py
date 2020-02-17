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

N = INT()
L = [S_LIST() for i in range(N)]
place = []
population = []
for l in L:
    place.append(l[0])
    population.append(int(l[1]))
tmp = 0
half = sum(population) / 2
ans = "atcoder"
for i in range(N):
    if population[i] > half and tmp != max(tmp, population[i]):
        tmp = max(tmp, population[i])
        ans = place[i]
print(ans)
        

