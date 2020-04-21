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

# for i in range(N):
# while 1:
#     S = str(N)
#     wa = 0
#     for i in range(len(S)):
#         wa += int(S[i])
    

S = str(N)
su = 0
# nine = "9" * (len(S)-1)
# a = "8" + nine
# b = "9" + nine
wa = 0
wa = 9 * (len(S) - 1) 
# if 
# print(wa)
# c = 9 - int(S[0])
# if S.count("9") == len(S):
#     print(9 * len(S))
if S[1:] == (len(S)-1) * "9":
    ans = 9 * (len(S)-1) + int(S[0])
    print(ans)
# elif len(S) == 1:
#     print(N)
else:
    ans = wa + int(S[0]) - 1
    # print(int(a))
    # print(wa)
    print(ans)