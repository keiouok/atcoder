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
from shapely.geometry import Polygon

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(float, input().split()))
def S_LIST(): return list(map(str, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

ax1, ay1, bx1, by1, cx1, cy1, dx1, dy1, ax2, ay2, bx2, by2, cx2, cy2, dx2, dy2 = MAP()

polygon_A = Polygon([(ax1, ay1), (bx1, by1), (cx1, cy1), (dx1, dy1)])
polygon_B = Polygon([(ax2, ay2), (bx2, by2), (cx2, cy2), (dx2, dy2)])

# intersection = polygon_A.intersection(polygon_B)
# if intersection.area == 0:
#     print("FALSE")
# else:
#     print("TRUE")
intersection = polygon_A.intersection(polygon_B)
area_A = polygon_A.area
area_B = polygon_B.area

if polygon_A.intersects(polygon_B):
    if intersection.area == area_A or intersection.area == area_B:
        print("FALSE")
    else:
        print("TRUE")
else:
    print("FALSE")