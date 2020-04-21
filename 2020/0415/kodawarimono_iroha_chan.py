import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

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

q = deque([""])

s = set([i for i in range(0, 10)]) 
d = set(D)
kouho = s - d
kouho = sorted(list(set(kouho)))
while q:
    a = q.popleft()
    # print(q)

    if len(a) != 0:
        if int(a) >= N:
            print(a)
            break
    for d in kouho:
        b = deepcopy(a)
        # if len(b) == 0 and d == 0:
        #     pass
        # else:
        b += str(d)
        q.append(b)
    

