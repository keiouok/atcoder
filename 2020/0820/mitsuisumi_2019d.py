import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left, bisect_right

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
L = input()
S = list(map(int, list(L)))

# print(S)
cnt = 0
# 000-999 1000
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            num = 0
            flag = False
            exist = [False] * 3
            while num != N and flag != True:
                # print(num)
                if exist[0] == False:
                    # print(S[num])
                    if S[num] != i:
                        num += 1
                    elif S[num] == i:
                        num += 1
                        exist[0] = True
                else:
                    if exist[1] == False:
                        if S[num] != j:
                            num += 1
                        elif S[num] == j:
                            num += 1
                            exist[1] = True
                    else:
                        if exist[2] == False:
                            if S[num] != k:
                                num += 1
                            elif S[num] == k:
                                num += 1
                                exist[2] == True
                                flag = True
            if flag == True:
                cnt += 1            
print(cnt)
                        
                