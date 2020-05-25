# atcoder

平衡状態は永遠に続く(茶⇄緑)

`make_dir.sh`
フォルダ自動作成．ABCの下などに置き，そこで実行．

## 参考文献

二次元配列

http://sonickun.hatenablog.com/entry/2014/06/13/132821

https://qiita.com/knakajima3027/items/b871631b8997a6d67223

[python] いろいろな文字種のリストを作成

https://qiita.com/okkn/items/3aef4458ed2269a59d63

## CheetSheet(updated on 2020/04/21)

```
import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
```

## list内をstring出力

2重リストの展開表示(要素がintの場合はaの部分にmapをかけてint型をstr型にキャストしておく)

```

a = [[".", "#", "."], ["#", "#", "#"]]
print(*["".join(x) for x in a], sep="\n")
```
出力結果
```
.#.
```

## 3 数以上の最小公倍数、最大公約数
```
def many_lcm(l):
    tmp = l[0]
    for i in range(1, len(l)):
        tmp = tmp * l[i]//gcd(tmp, l[i])
    return tmp
```

## 約数の列挙
```
def divisor(n): #nの約数を全て求める
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table
```
## 素因数分解
```
#nを素因数分解したリストを返す
def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table
```

## 素数判定
```
#引数nが素数かどうかを判定
def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1
```

## エラトステネスの篩
 O(nloglogn), 素数列挙
```
def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    return is_prime, table
```
## べき乗
```
#xのn乗をmで割った余り
def pos(x, n, m):
    if n == 0:
        return 1
    res = pos(x*x%m, n//2, m)
    if n%2 == 1:
        res = res*x%m
    return res
```

## bit生成
```
import itertools
L = [0, 1] #生成する数字
num = 3 #生成するビット数
bit_list = list(itertools.product([0, 1], repeat=num))
```

## 階乗
```
import itertools
seq = ('a', 'b', 'c', 'd', 'e')
ptr = list(itertools.permutations(seq)) #組み合わせ列挙 5!
ptr_num = len(list(itertools.permutations(seq))) #組み合わせ数 
```
実行結果
```
[('a', 'b', 'c', 'd', 'e'),
 ('a', 'b', 'c', 'e', 'd'),
 ('a', 'b', 'd', 'c', 'e'),
 ('a', 'b', 'd', 'e', 'c'),
           中略
 ('e', 'd', 'c', 'a', 'b'),
 ('e', 'd', 'c', 'b', 'a')]
120
```

## 順列
```
import itertools
seq = ('a', 'b', 'c', 'd', 'e')
ptr = list(itertools.permutations(seq, 3)) #順列列挙 5P3
ptr_num = len(list(itertools.permutations(seq, 3))) #順列数
```
実行結果
```
[('a', 'b', 'c'),
 ('a', 'b', 'd'),
 ('a', 'b', 'e'),
 ('a', 'c', 'b'),
       中略
 ('e', 'd', 'a'),
 ('e', 'd', 'b'),
 ('e', 'd', 'c')]
60
```
## 組み合わせ nCa
```
import itertools
seq = ('a', 'b', 'c', 'd', 'e')
ptr = list(itertools.combinations(seq,3)) # 組み合わせ列挙 5C3
```
実行結果
```
[('a', 'b', 'c'),
 ('a', 'b', 'd'),
 ('a', 'b', 'e'),
 ('a', 'c', 'd'),
 ('a', 'c', 'e'),
 ('a', 'd', 'e'),
 ('b', 'c', 'd'),
 ('b', 'c', 'e'),
 ('b', 'd', 'e'),
 ('c', 'd', 'e')]
```

## 数え上げ
```
from collections import Counter
arr = [1,1,4,6,1,1,35,1,5,1,3]
d = Counter() #インスタンスを生成
d.update(arr)
print(d[1]) #d[数えたい値]

```
実行結果
```
6
```

## 多次元配列のソート
```
A = [[1, 2], [3, 1], [2, 5]]
B = sorted(A, key=lambda x: x[0]) # 0番目の要素でソート
C = sorted(A, key=lambda x: x[1]) # 1番目の要素でソート
```
実行結果
```
B = [[1, 2], [2, 5], [3, 1]]
C = [[3, 1], [1, 2], [2, 5]]
```

## 二分探索
```
import bisect
#ソートされたリストAにソートを崩さずに値xを挿入するとき、xの入るべきインデックスを返す。
bisect.bisect(A,x)

#リストAに値xを入れ、xが複数になるとき、一番左の値xのインデックスを返す
bisect.bisect_left(A,x)

#リストAに値xを入れ、xが複数になるとき、一番右の値xのインデックスを返す
bisect.bisect_right(A,x)
```

## 整数屋の二分探索
ABC146C．整数屋の問題から自作．rightは[left, right)が半開区間となり，leftは含むがrightを含まないようにするために，right = x + 1にする必要がある．
```
# x = 持っているお金の金額
# 返すのは，お店で変える最大の整数N
# retは整数Nを買うのに必要な金額を返す関数

def binary_search(x):
    left = 0
    right = x + 1

    while(right - left > 1):
        mid = (right + left) // 2
        r = ret(a, b, mid)
        if r > x:
            right = mid
        else:
            left = mid
    return min(left, 10 ** 9)
```

## UnionFind(強い方を新調)
```
class UnionFind():
    def __init__(self, n):
        self.n = n
        # parents[i]: 要素iの親要素の番号
        # 要素iが根の場合、parents[i] = -(そのグループの要素数)
        self.parents = [-1] * n
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    # 要素xが属するグループの要素数を返す
    def size(self, x):
        return -self.parents[self.find(x)]
    def same(self, x, y):
        return self.find(x) == self.find(y)
    # 要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    # 全ての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    # グループの数を返す
    def group_count(self):
        return len(self.roots())
    # 辞書{根の要素: [そのグループに含まれる要素のリスト], ...}を返す
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    # print()での表示用
    # all_group_members()をprintする
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
```

## クラスカル法

```
#union-find木
#クラスカル法にはUnion-find木が必要
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)] #親
        self.rank = [0 for _ in range(n)] #根の深さ

    #xの属する木の根を求める
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    #xとyの属する集合のマージ
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    #xとyが同じ集合に属するかを判定
    def same(self, x, y):
        return self.find(x) == self.find(y)


#クラスカル法
# V: 頂点集合(リスト) E: 辺集合[始点, 終点, 重み](リスト)
class kruskal():
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.E.sort(key=lambda x: x[2]) #辺の重みでソート

    def weight(self): #最小全域木の重み和を求める
        UF = UnionFind(len(V)) #頂点数でUnion Find Treeを初期化
        res = 0
        for i in range(len(self.E)):
            e = self.E[i]

            if (UF.same(e[0], e[1])) == False:
                UF.unite(e[0], e[1])
                res += e[2]

        return res

    def edge(self):
        UF = UnionFind(len(self.V)) #頂点数でUnion Find Treeを初期化
        res_E = []
        for i in range(len(self.E)):
            e = self.E[i]

            if (UF.same(e[0], e[1])) == False:
                UF.unite(e[0], e[1])
                res_E.append(e)

        return res_E

    def node(self):
        UF = UnionFind(len(V)) #頂点数でUnion Find Treeを初期化
        res_V = []
        for i in range(len(E)):
            e = E[i]

            if (UF.same(e[0], e[1])) == False:
                UF.unite(e[0], e[1])
                res_V.append(e[0])
                res_V.append(e[1])

        return list(set(res_V))
```

## ワ―シャルフロイド法
```
#d[i][j]は2頂点間i, j間の移動コストを格納, Vは頂点数
def warshall_floyd(d, V): 
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d #d[i][j]に頂点i, j間の最短距離を格納
```

## 文字列生成
```
>>> import string
>>> help(string)
(中略)
DATA
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    hexdigits = '0123456789abcdefABCDEF'
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv...\xaf\xb0...
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    octdigits = '01234567'
    printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU...
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    whitespace = '\t\n\x0b\x0c\r '
>>> string.digits
'0123456789'
```

## アルファベット，英語，小文字
```
[chr(i) for i in range(97, 97+26)]
# [chr(i) for i in range(ord('a'), ord('z')+1)]
```

## 二次元配列，書き変わらないようにリスト内包で作成せよ

悪い例，他の要素の置き換わる
```
arr = [[0] * 10] * 10
```

いい例

```
arr = [[0 for i in range(10)] for j in range(10)]
```


## 素数列挙 O(NloglogN) (by tonnn*)
```
def primes_for(n):
  is_prime = [True] * (n + 1)
  is_prime[0] = False
  is_prime[1] = False
  for i in range(2, n + 1):
      for j in range(i * 2, n + 1, i):
          is_prime[j] = False
  return [i for i in range(n + 1) if is_prime[i]]
```
## ダイクストラ法
```
def dijkstra(E, start):
    N_d = len(E)
    dist = [INF] * N_d
    dist[start] = 0
    q = [(0, start)]
    while q:
        dist_v, v = heappop(q)
        if dist[v] != dist_v:
            continue
        for u, dist_vu in E[v]:
            dist_u = dist_v + dist_vu
            if dist_u < dist[u]:
                dist[u] = dist_u
                heappush(q, (dist_u, u))
    return dist
```
E は 連結リスト(多分) startは始点

E[a].append(b, c)

ABC035D．意味するのは，「a番目のノードがbと繋がっており，コストはc」 これが連結リスト．すべてのノードからダイクストラを求める必要はない．0スタートを逆順にすればよいだけ．大事．

## クリップボードにコピー
```
cat test.txt | xsel --clipboard --input
```

## 表とかリストを見やすくできる
```
print(*visited_copy, sep="\n")
```
## 壁を作る関数選手権で一位を取った関数
```
C = ["#"*(W+2)] + ["#"+C[i]+"#" for i in range(H)] + ["#"*(W+2)]
```
## Counterなどの辞書のソート 
```
d = sorted(d.items(), key=lambda pair: pair[1], reverse=True)
```

## 逆元とnCkと繰り返し二乗法

**ABC156D**
```
def power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x % mod
    elif y % 2 == 0:
        return power(x, int(y/2)) ** 2 % mod
    else:
        return power(x, int((y-1)/2)) ** 2 * x % mod
    
# nCaとしたときのaのmaxがa_max
a_max = 2 * 10 ** 5
# a, bの最大値+2
fact = [1] * (a_max + 2)
# 逆元
for i in range(1, a_max + 1):
    fact[i] = (fact[i-1] * i) % mod
# combination
def C(n, a):
    tmp = 1
    for i in range(n, n-a, -1):
        tmp = (tmp * i) % mod
    return tmp * power(fact[a], mod - 2)
```
## tonnn* version(上はバグることがあるのでこっち使おう)
```
upper = 10**6  # 必要そうな階乗の限界を入れる
factorial = [1]
for i in range(1, upper):
    factorial.append(factorial[i-1] * i % mod)
def power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x % mod
    elif y % 2 == 0:
        return power(x, int(y/2)) ** 2 % mod
    else:
        return power(x, int((y-1)/2)) ** 2 * x % mod
 
def C(n, r):
    return (((factorial[n] * x_inv[r]) % mod) * x_inv[n-r]) % mod
 
x_inv = [0] * upper
x_inv[-1] = power(factorial[-1], mod-2)
for i in range(upper-2, -1, -1):
    x_inv[i] = x_inv[i+1] * (i+1) % mod
``` 


## Priority Queue

**ABC141D_tickets**

最小値（最大値）を O(logN)で取り出す

要素を O(logN)で挿入する

```
N, M = MAP()
A = LIST()
A = list(map(lambda x: x * (-1), A))

heapq.heapify(A)
# print(A)

for i in range(M):
    a = heapq.heappop(A) * (-1)
    a = a // 2
    heapq.heappush(A, -a)
A = list(map(lambda x: x * (-1), A))
print(sum(A))
```

## accumulate
```
# 累積イテレータを生成
p = list(accumulate(num_list, mul))
p = list(accumulate(num_list, add))
```

## 組み合わせの総数
```
def combinations_count(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))
```