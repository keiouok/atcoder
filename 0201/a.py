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

n = INT()
W = [input() for i in range(n)]
real = []
image = []
for i in range(n):
    if not i % 2:
        # odd
        real.append(W[i])
    else:
        image.append(W[i])
# 同じ言葉
if len(real) != len(set(real)) and len(image) != len(set(image)):
    print("DRAW")
    exit()
elif len(real) != len(set(real)):
    print("LOSE")
    exit()
elif len(image) != len(set(image)):
    print("WIN")
    exit()

for i in range(n-1):
    if W[i+1][0] != W[i][-1]:
        if (i + 1) % 2 == 0:
            # real lose
            print("LOSE")
            exit()
        else:
            print("WIN")
            exit()
print("DRAW")



    

