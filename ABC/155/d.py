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

N, K = MAP()
a = LIST()
a.sort()
A = deque(a)

left = 0
right = N-1
T = []
tmp = INF

    # 最初

plus = []
minus = []
zero = 0

for i in range(N):
    if a[i] > 0:
        plus.append(a[i])
    elif a[i] < 0:
        minus.append(a[i])
    elif a[i] == 0:
        zero += 1
plus.sort()
minus.sort()
print(len(plus))
print(len(minus))
print(zero)

# one
one = plus * minus
two = one + zero
count = 0
if K <= one:
    count += 1
    T.append(A[left] * A[right])

    ans = minus.popleft() * plus.pop()
    if count == K:
        print(ans)
        exit()

    while left != right:
        a = A[left] * A[right - 1]
        b = A[right] * A[left + 1]
        if a <= b
    




# print(A)
# print(A.popleft())
# print(A.pop())


# A = LIST()

# A.sort()
# l = list(combinations(A ,2))

# print(A)

# L = []
# for k in l:
#     a,b = k[0], k[1]
#     L.append(a * b)
# L.sort()

# print(L[K-1])
