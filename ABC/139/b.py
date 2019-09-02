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

a, b = MAP()
ans = 0
# if b == 1:
#     print(ans)
#     exit()
if b == 1:
    print(ans)
    exit()


while(1):

    if ans == 0:
        b -= a
        ans += 1
    else:
        if b <= 0:
            print(ans)
            exit()
        else:
            b -= (a-1)
            ans += 1

    

# n = INT()
# a, b, c = MAP()
# ans = 1
# # count = 0
# count = a
# flag = False
# # for i in range(30):
# while flag == False:
#     if count >= b:
#         flag = True    
#     else:
#         count += a-1
#         ans += 1
# print(ans)





# k = 1
# count = 0
# ans = 0
# A = []


# count += a
# ans += 1


# while(1):
#     if count >= b:
#         print(ans)
#         exit()
#     else:
#         count += a-1
#         ans += 1
#         # print()




# count += a
# ans += 1

# for i in range(100):
#     if b <= count:
#         print(ans)
#         exit()

#     else:
#         count += a-1
#         ans += 1 
#         # print(ans)

# for i in range(30):
# while(1):
#     count += a
#     ans += 1
#     print(count)

#     if b <= count:
#         print(ans)
#         exit()
#     else:   
#         count = count-1
#     # print(ans)
    
    # # A.append(a)
    # # if sum(A)
    # if count == 0:
    #     count += a
    #     ans += 1
    # else:
    #     count += a-1
    #     ans += 1
    # print(count)
    # print(ans)
    # if b<=count:
    #     # print(count)
    #     print(ans)
    #     exit()

