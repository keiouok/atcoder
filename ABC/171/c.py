import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
A =[chr(i) for i in range(97, 97+26)]
# print(A)
L = []
while 1:
    a = N % 26
    N = N // 26
    # N -= 1
    if a == 0:
        N -= 1
    
    # print(a)
    # if a == 0:
    #     L.append(26)
    # else:
    L.append(a)
    if N <= 0:
        break
ans = ""
L.reverse()
for a in L:
    ans += A[a-1]
print(ans)





exit()
def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+","+out
        X_dumy = X_dumy//n
    return out
# while N:
# while N:
#     a = N % 26
#     N = N // 26
#     print(a)
ans = Base_10_to_n(N, 26)
l = ans.split(",")
print(l)
ans = ""
r = l[:-2]
if Counter(r)["1"]==len(r) and l[-2] == "0":
    # print(r)
    print("z" * (len(r)))
    exit()
#  == len(l[:-1]) and l[-1] == "0":
    # print(l)
    # exit()
for a in l:
    if len(a) != 0:
        a = int(a)
        # if a == 0:
        #     ans += "z"
        # else:

        tmp = A[a-1]
        ans += tmp

print(ans)