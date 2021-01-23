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
A = LIST()

C = Counter(A)
mi = min(A)
left = 0
ans = 0

# q = deque(A)


ans = mi * len(A)

L = [0] * N

C = sorted(C.keys())
# print(C)
q = deque(C)

l = 0
r = N - 1
mi = A[l]

dic = defaultdict(list)

for i, a in enumerate(A):
    dic[a].append(i)
print(dic)

D = sorted(dic, reverse=True)
print(D)

for d in D:
    sd = sorted(d)
    for i, y in range(len(sd)-1):
        if sd[i+1] == sd[i] + 1:
            



# exit()
# y = tuple(l, r, mi, mi * (r - l) + 1)
# q = deque([y])

# while q:
#     a = q.popleft()
#     l, r, mi, tmp = a
#     while l < r:
#         l += 1
#         if l != mi







    



exit()
while q:
    mi = q.popleft()
    L = [0] * N
    for i, a in enumerate(A):
        if a >= mi:
            # L.append(i)
            L[i] += 1
    # tmp = 0
    # print(L)
    tmp = L[0]
    for i in range(1, N):
        if L[i-1] != 0 and L[i] != 0:
            L[i] = L[i-1] + 1
        if L[i] > tmp:
            tmp = L[i]
    # print(tmp, mi)
    ans = max(ans, tmp * mi)
    # print(L)
print(ans)





exit()
mi = A[left]
ans = mi
for right in range(1, N):
    while 1:
        if mi > A[right]:
            mi = A[right]
        l = mi * (right - left + 1)
        r = A[right] * (right - left)

#     gap = right - left
#     ans = max(ans, mi * gap)
#     if A[right] > A[left]:
#     # mi2 = A[right]
#     right += 1
# print(ans)
    



