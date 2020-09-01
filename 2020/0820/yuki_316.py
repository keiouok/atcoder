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

N = INT()
A = LIST()

def many_lcm(l):
    tmp = l[0]
    for i in range(1, len(l)):
        tmp = tmp * l[i]//gcd(tmp, l[i])
    return tmp

# a = N // 3 + N // 5 - N // 15
# print(a)
# exit()
mi = many_lcm(A)
a = many_lcm(A[0:2])
b = many_lcm(A[1:3])
c = many_lcm([A[0], A[2]])
# print(a, b, c)
# print(mi)

ans = N // A[0] + N // A[1] + N // A[2] - N // a - N // b - N // c + N // mi
print(ans)