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

A = input()
N = int(A)

if len(A) == 1:
    if int(A) == 8:
        print("Yes")
        exit()
elif len(A) == 2:
    if int(A[0] + A[1]) % 8 == 0 or int(A[1] + A[0]) % 8 == 0:
        print("Yes")
        exit()
else:
    L = list(permutations(list(A)))
    # print(L)
    for l in L:
        n = int("".join(l))
        # print(n)
        if n % 8 == 0:
            print("Yes")
            exit() 
#         a = list(permutations(l))
#         for y in a:
#             shimo = int("".join(y))
#             if shimo % 2 != 0:
#                 continue
#             ni = shimo // 2
#             b = int(str(ni)[-3:])
#             if b % 4 == 0:
#                 print("Yes")
#                 exit()
print("No")