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

s = input()
s = deque(s)
q = INT()

r_count = 0
L = [S_LIST() for i in range(q)]
for i in range(q):
    if L[i][0] == "1":
        r_count ^= 1
        # s.reverse()
    else:
        query, sent = int(L[i][1]), str(L[i][2])
        if r_count == 0:
            if query == 1:
                s.appendleft(sent)
            else:
                s.append(sent)
        else:
            if query == 2:
                s.appendleft(sent)
            else:
                s.append(sent)

if r_count != 0:
    s.reverse()
print("".join(list(s)))
    
    


