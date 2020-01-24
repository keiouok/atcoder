# 要復習
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

def main():
    N = INT()
    uv = [LIST() for i in range(N - 1)]

    # graphがあればまずグラフを辞書で書く
    graph = defaultdict(list)

    # 辺，edge，key: ，value:色情報
    edge = defaultdict(int)

    for u, v in uv:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    K = 0
    for v in graph.values():
        # 最も長いリストの長さになる
        K = max(K, len(v))
    color = list(range(1, K + 1))
    
    # 使う色の数，これだけつかえばいい
    # print("K", K)
    # print("color:", color)
    que = deque()
    que.append((0, None))

    # bfs
    # use_color:その辺で使うカラー
    while que:
        i, color_from = que.popleft()
        tmp = -1
        for node in graph[i]:
            str_ = "{},{}".format(i, node)
            if not edge[str_]:
                # 一番最後のカラー
                use_color = color[tmp]
                if use_color == color_from:
                    # 同じなら，一番最後から前に下がっていく
                    use_color = color[tmp - 1]
                    tmp -= 1
                tmp -= 1

                edge[str_] = use_color
                # 逆も然り
                edge["{},{}".format(node, i)] = use_color
                que.append((node, use_color))
    print(K)
    for u, v in uv:
        print(edge["{},{}".format(u-1, v-1)])


if __name__ == "__main__":
    main()


