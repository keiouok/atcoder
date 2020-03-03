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

N = INT()
A = LIST()
# ball を入れたら1
ball = [0] * (N + 1)

for i in range(len(A), 0, -1):
    if i > N // 2:
        ball[i] = A[i-1]
    else:
        tmp = A[i-1]
        for x in range(i, N+1, i):
            if x == i:
                continue
            tmp = tmp ^ ball[x]
        ball[i] = tmp

print(sum(ball))

exit()
for i in range(N):
    # last
    small_real = i+1
    big = N-1-i
    amari = A[big]
    big_real = N - i
    big_real
    wa_now = 0 
    while big_real <= N:
        wa_now += A[big_real-1]
        print(big_real)
        big_real = big_real + big_real
        
    # print(wa_now)
    if wa_now % big_real != A[big]:
        ball[big] += 1
print(ball)





