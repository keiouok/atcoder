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

N, M , W = MAP()
A = LIST()
B = LIST()

sa = sum(A)
sb = sum(B)
A.reverse()
C = A + B
# print(C)
ans = 0
left_wa = 0
right_wa = 0


ruiseki = C.copy()
# ruiseki = [0] + ruiseki
for i in range(len(ruiseki)-1):
    ruiseki[i+1] = ruiseki[i] + ruiseki[i+1]
# print(ruiseki)
# ruiseki = ruiseki + [ruiseki[-1]]
left = 0
# for right in range(1, len(C)+1):
#     ruiseki[left:right]
idx = 0
wa = 0
ans = 0
# print(len(ruiseki))
if sum(A) + sum(B) <= W:
    print(N + M)
    exit()
for right in range(len(A), len(ruiseki)):
    # idx += 1
    # print("right:", right)
    wa = ruiseki[right] - ruiseki[left]
    # if
    while wa > W:
        left += 1
        wa = ruiseki[right] - ruiseki[left]
    if left < len(A):
        tmp = right - left
        # print(tmp)
        ans = max(tmp, ans)
        # print("left, right:", left, right)
    
    else:
        break
    # print("left, right, :", left, right)

print(ans)        






exit()
for right in range(1, N+1):
    # sum(A[left:right])
    right_wa += C[right-1]
    wa = right_wa - left_wa
    if wa <= K:
        while wa <= K:
            if left < N:
                left_wa += C[left]
                wa = right_wa - left_wa
            left += 1
    ans += left
    



exit()
A = deque(A)
B = deque(B)

# C = A + B
cnt = 0
while W >= 0 and cnt != N + M:
    if len(A) != 0 and len(B) != 0:
        a = A[0]
        b = B[0]
        if a <= b:
            W -= a
            A.popleft()
        else:
            W -= b
            B.popleft()
    elif len(A) != 0:
        # a = INF
        a = A.popleft()
        W -= a
    elif len(B) != 0:
        # a = INF
        b = B.popleft()
        W -= b
    # print(W)
    if W >= 0:
        cnt += 1


print(cnt)



# 3 4 240
# 60 90 120
# 80 150 80 150
# 出力例 1 
