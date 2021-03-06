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

N, K = MAP()
A = LIST()

ruiseki = [0] * (N + 1)
for i in range(N):
    ruiseki[i+1] = ruiseki[i] + A[i]
# print(ruiseki)

right_wa = 0
left_wa = 0
right = 0
left = 0
ans = 0
for right in range(1, N+1):
    right_wa += A[right-1]
    wa = right_wa - left_wa
    if wa >= K:
        while wa >= K:
            if left < N:
                left_wa += A[left]
                wa = right_wa - left_wa
            left += 1
    ans += left
print(ans)



# left = 0
# for right in range(N)
exit()
left = 0
wa = 0
ans = 0
right = 0

while right < N:
    wa += A[right]
    if wa >= K:
        # ans += 1
        
        while wa >= K:
            ans += 1  
            # print(wa)
            wa -= A[left]
            left += 1
    # else:
    right += 1

print(ans)




        

        


