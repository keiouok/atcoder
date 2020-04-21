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

N = INT()

q = ["3", "5", "7"]

ans_list = []
ans = 0
while q:
    a = q.pop()

    if len(a) != 0:
        if int(a) <= N:
            cnt = 0
            for i in [3, 5, 7]:
                if a.count(str(i)) >= 1:
                    cnt += 1
            if cnt == 3:
                ans += 1
                ans_list.append(a)

        
            for i in [3, 5, 7]:
                b = deepcopy(a)
                b += str(i)
                q.append(b)

print(ans)
# print(ans_list)