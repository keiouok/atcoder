import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from heapq import heapify, heappop, heappush
 
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
ans = 0
yowa = 0
tuyo = 0
dic = defaultdict(int)
d = [0] * 8
for a in A:
    if a < 3200:
        if 1 <= a <= 399:
            d[0] = 1
        elif 400 <= a <= 799:
            d[1] = 1
        elif 800 <= a <= 1199:
            d[2] = 1
        elif 1200 <= a <= 1599:
            d[3] = 1
        elif 1600 <= a <= 1999:
            d[4] = 1
        elif 2000 <= a <= 2399:
            d[5] = 1
        elif 2400 <= a <= 2799:
            d[6] = 1
        elif 2800 <= a <= 3199:
            d[7] = 1
    else:
        tuyo += 1

al = sum(d)

if tuyo >= 1:
    if al >= 1:
        mi = al
    else:
        mi = 1
else:
    mi = al
ma = 0
if tuyo >= 1:
    zero_num = 7 - al
    if tuyo >= zero_num:
        ma = 7
    else:
        zero_nokori = (zero_num - tuyo)
        ma = 7- zero_nokori

else:
    ma = al

print(mi, ma)
exit()
if tuyo == 0:
    mi = al
elif tuyo >= 1:
    if al >= 1:
        mi = al
    else:
        mi = 1
# no zero in d
zero = 7 - al    

mx = min(7, 7-(zero-tuyo))
print(mi, mx)


        


