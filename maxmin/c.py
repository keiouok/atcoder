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


N = INT()
A = LIST()
dic = defaultdict(int)

ans = -INF
for i in range(N):
    # takahashi kotei by i
    taka = A[i]
    # taka_list = defaultdict(list)
    dic = defaultdict(list)
    for j in range(N):
        if i != j:
            if i < j:
                T = A[i:j+1]
            else:
                T = A[j:i+1]
            # print(T)
            taka, ao = 0, 0
            for k in range(len(T)):
                if k % 2 == 0:
                    # kisu, takahashi
                    taka += T[k]                        
                else:
                    ao += T[k]
            dic[ao].append(taka)        
    # ao が最大となる中でtakaがminのものは
    dic = sorted(dic.items(), key=lambda x : x[0], reverse=True)
    ao_max, taka_list = dic[0]
    # print(dic)
    taka_min = taka_list[0]
    # その中で一番大きいもの
    if ans <= taka_min:
        ans = taka_min
print(ans)


       