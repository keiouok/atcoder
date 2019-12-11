import pdb
import heapq
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
def Yes(): print("Yes")
def YES(): print("YES")
def No(): print("No")
def NO(): print("NO")

sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

S = input()
T = INT()

count = 0

if T == 1:
    # max
    x = 0
    y = 0
    for s in S:
        if s == "?":
            count += 1
        if s == "U":
            y += 1
        if s == "D":
            y -= 1
        if s == "L":
            x -= 1
        if s == "R":
            x += 1
    print(abs(x) + abs(y) + count)

elif T == 2:
    # min
    x = 0
    y = 0
    for s in S:
        if s == "?":
            count += 1
        if s == "U":
            y += 1
        if s == "D":
            y -= 1
        if s == "L":
            x -= 1
        if s == "R":
            x += 1
    
    # if x <= 0:
    # if abs(x) + abs(y) >= count:
    #     ans = abs(x) + abs(y) - count
    # else:
    #     ans = count - (abs(x) + abs(y))
    # print(ans)
    # print(count)
    while count != 0:
        if x < 0 and count > 0:
            x += 1
            count -= 1
            # print("a")
            # print(x)
            # print(count)
        elif x > 0 and count > 0:
            x -= 1
            count -= 1
            # print("b")
            # print(x)
        elif y < 0 and count > 0:
            y += 1
            count -= 1
            # print("c")
            # print(y)
        elif y > 0 and count > 0:
            y -= 1
            count -= 1
            # print("d")
            # print(y)
        if x == 0 and y == 0:
            ans = count
            # print("e")
            print(ans % 2)
            exit()
    ans = abs(x) + abs(y)

    print(ans)



