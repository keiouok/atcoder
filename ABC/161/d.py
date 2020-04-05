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

K = INT()

q = [str(i) for i in range(1, 10)]
q = deque(q)
# print(q)

l = []
while len(l) != K:
    a = q.popleft()
    l.append(a)
    for i in range(0, 10):
        last = int(a[-1])
        b = deepcopy(a)
        if last == 0:
            if i == 1 or i == 0:
                b = b + str(i)
                q.append(b)
        elif last == 9:
            if i == 8 or i == 9:
                b = b + str(i)
                q.append(b)
        else:
            if last - 1 <= i <= last + 1:
                b = b + str(i)
                q.append(b)
        
        # print(q)
        # exit()
print(l[-1])