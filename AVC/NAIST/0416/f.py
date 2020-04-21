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
ans = 0
dic = defaultdict(int)
i = 0
hoge = 0
for s in S:
    if s == "J":
        if dic["O"] == 0 and dic["I"] == 0:
            dic["J"] += 1
        else:
            dic["J"] = 1
            dic["O"] = 0
            dic["I"] = 0
    elif s == "O":
        if dic["J"] >= dic["O"] and dic["I"] == 0:
            dic["O"] += 1
        else:
            dic["J"] = 0
            dic["O"] = 0
            dic["I"] = 0
    elif s == "I":
        if dic["O"] > 0:
            dic["I"] += 1
            if dic["J"] >= dic["O"] and dic["O"] <= dic["I"]:
                ans = max(ans, dic["O"])
        else:
            dic["J"] = 0
            dic["O"] = 0
            dic["I"] = 0
print(ans)
            






exit()
for i in range(N):
    if S[i] == "J":
        dic["J"] += 1
    elif i > 0:
        if (S[i] == "O" and S[i-1] == "J")\
            or S[i] == "O" and S[i-1] == "O":
            dic["O"] += 1
    elif i > 0:
        if (S[i] == "I" and S[i-1] == "O")\
            or S[i] == "I" and S[i-1] == "I":
            dic["I"] += 1
            if i + 1 < N:
                if S[i+1] != "I":
                    if dic["J"] >= dic["O"] and \
                        dic["O"] <= dic["I"]:
                        print(dic)
                        ans = max(ans, dic["O"])
                        dic = defaultdict(int)

            elif i == N - 1:
                if dic["J"] >= dic["O"] and \
                    dic["O"] <= dic["I"]:
                    ans = max(ans, dic["O"])
                    dic = defaultdict(int)
print(ans)

    




