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

H, W, K = MAP()
S = [list(input()) for i in range(H)]
int_S = []
print(S)
for i in range(H):
    l = []
    for j in range(W):
        print(S[j])
        # l.append(int(S[j]))
    # int_S.append(l)

print(int_S)
exit()
tate_wa = [0] * W
# |||||||
yoko_wa = [0] * H

for i in range(H):
    sum()


for h in range(0, H):
    up = [0] * W
    down = [0] * W
    print(S[:h])
    print(S[h:])
    for w in range(0, W):
        up




