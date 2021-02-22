import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
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


def many_gcd(numbers):
    return reduce(gcd, numbers)


def many_lcm(l):
    tmp = l[0]
    for i in range(1, len(l)):
        tmp = tmp * l[i]//gcd(tmp, l[i])
    return tmp

def divisor(n): #nの約数を全て求める
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

K = INT()


cnt = 0

D = divisor(K)
D.sort(reverse=True)
print(D)
for i, d in enumerate(D):    
    bc_max = K // d
    dv = divisor(bc_max)
    print("dv:", dv)
    dv.sort(reverse=True)

    for j, b_max in enumerate(dv):
        if j == 0:
            cnt = b_max
        else:
            bmax_p = dv[j-1] # big
            bmax_c = dv[j] # small
            cmax_p = bc_max // bmax_p
            cmax_c = bc_max // bmax_c
            # 被り
            kabri = bmax_c * cmax_p
            # c_max = bc_max // b_max
            # cnt += 
            cnt += cmax_c * bmax_c - kabri            

        # c_max = bc_max // b_max
        # mi = min(c_max, b_max)
        # cnt += c_max * b_max
    # cnt += sum(dv)
print(cnt)

# for a in range(1, K + 1):
#     if K % a == 0:
#         bc = K // a
#         print(bc)
#         cnt += len(divisor(bc))
# print(cnt)


exit()
i = 1
while 1:
    if i * i * i > K:
        break
    i += 1

print(i) 
ma = i
print(ma)
cnt = 0
for i in range(1, ma+1):
    for j in range(1, ma+1):
        for k in range(1, ma+1):
            if i * j * k <= K:
                cnt += 1
print(cnt)


