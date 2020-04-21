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

S = input()
N = len(S)
dic = defaultdict(int)
ans = 0
for i in range(N):
    if S[i] == "J":
        dic[S[i]] += 1
    if S[i] == "O":
        if dic["J"] > dic["O"]:
            dic["O"] += 1
    if S[i] == "I":
        if dic["O"] > dic["I"]:
            dic["I"] += 1
    if dic["J"] >= dic["O"] >= dic["I"]:
        ans = max(dic["I"], ans)
        dic = defaultdict(int)
    print(dic)
print(ans)
# print(dic)
ruiseki = [[0] * (N + 1) for i in range(3)]

for i in range(N):
    if S[i] == "J":
        ruiseki[0][i+1] = ruiseki[0][i] + 1
        ruiseki[1][i+1] = ruiseki[1][i]
        ruiseki[2][i+1] = ruiseki[2][i]
    if S[i] == "O":
        ruiseki[0][i+1] = ruiseki[0][i]
        ruiseki[1][i+1] = ruiseki[1][i] + 1
        ruiseki[2][i+1] = ruiseki[2][i]
    if S[i] == "I":
        ruiseki[0][i+1] = ruiseki[0][i]
        ruiseki[1][i+1] = ruiseki[1][i]
        ruiseki[2][i+1] = ruiseki[2][i] + 1
    if ruiseki[0][i] >= ruiseki[]
print(*ruiseki, sep="\n")   
ans = 0
for i in range(N):
    # for j in range(N):
    tmp = min(ruiseki[0][i], ruiseki[1][i], ruiseki[2][i])
    ans = max(tmp, ans)

print(ans)


exit()
for i in range(N):
    if S[i] == "J":
        dic[S[i]] += 1
        ruiseki[0][i+1] = ruiseki[0][i] + 1

    if S[i] == "O":
        
        if dic["J"] > dic["O"]:
            dic["O"] += 1
    if S[i] == "I":
        if dic["O"] > dic["I"]:
            dic["I"] += 1
    if dic["J"] >= dic["O"] >= dic["I"]:
        ans = max(dic["I"], ans)
        # dic = defaultdict(int)
print(ans)