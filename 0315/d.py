# なぜかうまくいかない
import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_right, bisect_left

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
A = LIST()
# 0 0 0の左
zero = A.count(0)
# A.(0)
l = bisect_left(A, 0)
r = bisect(A, 0)
zero = r - l
C = []
for a in A[:l]:
    if a == 0:
        continue
    C.append(a)
    
B = C + A[r:]


w = K - zero
ans = INF
B.insert(0, -INF)
B.append(INF)
if zero == K:
    print(0)
    exit()

for i in range(len(B) - K + 1):
    r = B[i + K - zero - 1]
    l = B[i]
    tmp = INF
    if l < 0 and r > 0:
        tmp = min(abs(l), r) + r - l
    # ans = min(ans, tmp)
    elif l > 0 and B[i-1] < 0:
        # tmp = min(abs(l), r) + r - l
        tmp = r

    elif r < 0 and B[i + K - zero - 1 + 1] > 0:
        # tmp = min(abs(l), r) + r - l
        tmp = abs(l)
    ans = min(ans, tmp)
print(ans)


        # if abs(B[i]) <= :

#         tmp = B[i + K - zero-1] - B[i]
#         print(B[i+K-zero-1])
#         print(B[i])
#         ans = min(ans, tmp)
# print(ans)