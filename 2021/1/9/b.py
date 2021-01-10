import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """xの親を返す"""
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """yをxの根に繋ぐ（マージテク有）"""
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        """xとyが同じ連結成分か判別する"""
        return self.find(x) == self.find(y)

    def size(self, x):
        """xの連結成分の大きさを返す"""
        return -self.parents[self.find(x)]

    def kruskal(self, edge):
        """
        :param edge: edge = [(コスト, 頂点1, 頂点2),...]の形で重み付き隣接リストを渡して下さい
        :return: 最小全域木のコストの和
        """
        edge.sort()
        cost_sum = 0
        for cost, node1, node2 in edge:
            if not self.same(node1, node2):
                cost_sum += cost
                self.union(node1, node2)
        return cost_sum


def resolve():
    n = int(input())
    AB = [list(map(int, input().split())) for _ in range(n)]

    nums = sorted(set(a for a, _ in AB) | set(b for _, b in AB))
    m = len(nums)
    uf = UnionFind(m)
    for a, b in AB:
        i = bisect_left(nums, a)
        j = bisect_left(nums, b)
        uf.union(i, j)

    edge = [0] * m
    for a, b in AB:
        i = bisect_left(nums, a)
        root = uf.find(i)
        edge[root] += 1

    res = 0
    for i in range(m):
        root = uf.find(i)
        if root == i:
            res += min(edge[i], uf.size(root))
    print(res)


if __name__ == '__main__':
    resolve()
