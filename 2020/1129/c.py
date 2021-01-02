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
def LIST(): return list(map(float, input().split()))
def S_LIST(): return list(map(str, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

table = []

while 1:
    line = input()
    if len(line) == 0:
        break
    table.append(line)
print(table)

def hour_to_second(time):
    h, m, s = time.split(":")
    h = float(h)
    m = float(m)
    s = float(s)
    second = h * 3600 + m * 60 + s
    return second

htom = defaultdict(float)

for line in table:
    time, dist = line.split(" ")
    print(time, dist)
    print(hour_to_second(time))
    htom[time] = hour_to_second(time)

cost = 0
total_dist = 0
hatsunori = False
for line in table:
    time, dist = line.split(" ")
    total_dist
    if total_dist < 1.052:
        cost = 410
        

        



    
