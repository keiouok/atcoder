# なぜかうまくいかない
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

D, G = MAP()
pc = [LIST() for i in range(D)]

B = list(product([0, 1], repeat=D))

ans = INF
for b in B:
    point = 0
    count = 0
    for i, vonus in enumerate(b):
        if vonus == 1:
            # take all with vonus
            point += pc[i][0] * (i + 1) * 100 + pc[i][1]
            count += pc[i][0]
        # print(count)
    if point >= G:
        ans = min(count, ans)
        # print(count)
    else:
        # 後ろから
        need_point = G - point
        added_count = count
        for i in range(len(b)-1, -1, -1):
            if b[i] == 0:
                # while need_point > 0:
                    # count_max = pc[i][0]
                    num = ceil(need_point / (100 * (i + 1)))
                    if num >= pc[i][0]:
                        ###?
                        count = INF
                        break
                    count += ceil(need_point/ ((i+1) * 100))
                    break
                    # if need_point - point_max >= 0:
                    #     need_point -= point_max
                    #     count += count_max
                    # else:
                    #     count += ceil(need_point / (100 * (i + 1)))
                    #     need_point -= point_max
        ans = min(ans, count)
print(ans)


                
    
        # 超えてないならもうちょい必要

