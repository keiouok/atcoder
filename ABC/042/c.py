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
D = LIST()
d_s = set(D)
moto = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
amari = d_s & moto
l = list(str(N))
l = map(int, l)

# for i in range(len(l)):
i = N
while 1:
    
    l = list(str(i))
    l = list(map(int, l))
    l_s = set(l)
    s_intersection = d_s & l_s
    
    if len(s_intersection) == 0:
        print(i)
        exit()
    i += 1
    # if d_s.isdisjoint(l_s):
    #     print(i)
    #     exit()




