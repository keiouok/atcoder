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


def bubble_sort(A):
    cnt = 0
    for i in range(len(A)):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                cnt += 1
    return cnt

N, K = MAP()
A = LIST()

B = []
for i in range(2):
    for a in A:
        B.append(a)
# print(B)
tenchi1 = bubble_sort(A)
tenchi2 = bubble_sort(B)

ni = tenchi2-2*tenchi1
# print(ni)

# tenchi = bubble_sort(A)
# print(tenchi)
# wa1 = 0.5 * (K) * (K+1)
wa2 =  (K) * (K-1) / 2
# wa2 = wa2
# ans1 = wa1 * tenchi1
# print("wa1", wa1)
# print("wa2", wa2)
# print("tenchi1", tenchi1)
# print("tenchi2", tenchi2)
# print("ni", ni)
ans1 = K*tenchi1
ans2 = wa2 * ni
ans = ans1 + ans2

ans = ans % mod
print(ans)
