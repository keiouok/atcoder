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

A = list(input())
A.reverse()
B = list(input())
B.reverse()
C = list(input())
C.reverse()
player = A.pop()
while 1:
    # if len(A) == 0:
    #     print("A")
    #     exit()
    # if len(B) == 0:
    #     print("B")
    #     exit()
    # if len(C) == 0:
    #     print("C")
    #     exit()
    # print(player)
    if player == "a":
        if len(A) == 0:
            print("A")
            exit()
        else:
            player = A.pop()
    elif player == "b":
        if len(B) == 0:
            print("B")
            exit()
        else:
            player = B.pop()
    elif player == "c":
        if len(C) == 0:
            print("C")
            exit()
        else:
            player = C.pop()

    