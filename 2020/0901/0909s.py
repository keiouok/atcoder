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

Ans = []
while 1:
    N = INT()
    if N == 0:
        break
    q = deque([])
    for i in range(1, 10):
        # 10, ... , 19
        q.append(str(i))
    ans = []
    cnt = 0
    while 1:
        a = q.popleft()
        a_s = str(a)
        a_l = list(str(a))
        # if len(a) != 1:
        #     ans.append(a)
        print(len(ans))

        if len(ans) == N:
            print(len(ans))
            print(ans[0:390])
            Ans.append(ans.pop())
            print(Ans)
            break
        for i in range(0, 10):
            new_num = a_s + str(i)
            l = list(new_num)
            if len(set(l)) == 2:
                ans.append(a_s)
            q.append(new_num)

        
            



