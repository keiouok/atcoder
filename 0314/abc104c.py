import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left, bisect_right

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
# Dは2なら1 << Dは4
# bit全探索
print(1 << D)
count_min = 10 ** 9
for i in range(1<<D):
    sum_ = 0
    count = 0
    i = list("{:b}".format(i).zfill(D))
    # D = 2
    print(i)
    for j in range(D):
        # 1つずつ見る
        if i[j] == "1":
            # 1だったら全部加える
            sum_ += (j + 1) * 100 * pc[j][0] + pc[j][1]
            # そのまま全部の回数足す
            count += pc[j][0]
    if sum_ >= G:
        # 全部加えて今のところ超えてたら更新する
        if count < count_min:
            count_min = count
    else:# G - sum_ > 0
        for j in range(D-1, -1, -1):
            if i[j] == "0":
                # 中途半端にとる
                # あと必要な回数num
                num = ceil((G - sum_) / ((j + 1) * 100))
                
                if num > pc[j][0]:
                    count = 10 ** 9
                    break
                print("num:", num)
                count += ceil((G-sum_)/((j+1) * 100))
                break
        if count < count_min:
            count_min = count
print(count_min)


