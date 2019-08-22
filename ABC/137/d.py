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

n, m = MAP()
l = []
for i in range(n):
    d = LIST()
    l.append(d)
print(l)
above = m
s = l
# s = 
# for i in range(n):
#     if l[i][0] <= m:
#         s.append(l[i])
# s.sort()
s = sorted(s,key = lambda s: (s[0], s[1]), reverse = True)
print(s)

# zettai_day = 0
# for today in range(n):
#     zettai_day = today+1
count = 0
print(above)
while len(s) != 0:
    print("above",above)
    kesu_index = []
    for i in range(len(s)):
        print("s[i][0]",s[i][0])
        # s_x = s[i][0] + 1
        # s[i] =[s_x, s[i][1]]

        if s[i][0]>above:
            s.pop(i)
    print("s", s)
        #     print(s[i])
        #     kesu_index.append(i)
        # print(kesu_index)
        # print("kesumae", s)
        # s.pop(i)
    # print(s)
    if len(s) != 0:
        # if s[0][0]
        count += s[0][1]
        print(count)
        s.pop(0)
    s = sorted(s,key = lambda s: (s[0], s[1]), reverse = True)
    above += 1

print(count)

        

    
    

