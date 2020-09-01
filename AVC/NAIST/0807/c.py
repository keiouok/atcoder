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

H, W = MAP()
L = [list(input()) for i in range(H)]
# print(L)
# Counter(L)
dic = defaultdict(int)

for i in range(H):
    for j in range(W):
        dic[L[i][j]] += 1
print(dic)

dic = sorted(dic.items(), key=lambda pair: pair[1], reverse=True)
print(dic)
if H % 2 == 0 and W % 2 == 0:
    if H == 2 and W == 2:
        for v in dic.values():
            if v % 2 != 0:
                print("No")
                exit()
    else:
        for v in dic.values():
            if v % 4 != 0:
                print("No")
                exit()
    print("Yes")

elif H % 2 != 0 and W % 2 != 0:
    if H == 1 and W == 1:
        print("Yes")
        exit()
    else:
        four = 0
        # for v in dic.items():
        four = (W - 1) // 2 * (H - 1) // 2
        two = 2
        one = 1

    for a in [chr(i) for i in range(ord('a'), ord('z')+1)]:
        if dic[a] % 4 == 0:
            four -= 1
            dic[a] -= 4
        elif dic[a] % 2 == 0:
            two -= 1
            dic[a] -= 2
        elif dic[a] % 1 == 0:
            one -= 1
            dic[a] -= 1
    if four == two == one == 0 and sum(dic.values()) == 0:
        print("Yes")
    else:
        print("No")

