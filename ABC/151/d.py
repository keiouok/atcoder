from collections import deque

H, W = map(int, input().split())
maze = [list(input()) for i in range(H)]
# print(maze)
n = H
m = W

# (sx, sy) から (gx, gy) への最短距離を求める
# 辿り着けないと INF
def bfs(sx, sy):
    # すべての点を INF で初期化
    d = [[float("inf")] * m for i in range(n)]

    # 移動4方向のベクトル
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # for i in range(n):
    #     for j in range(m):
    #         # スタートとゴールの座標を探す
    #         if maze[i][j] == "S":
    #             sx = i
    #             sy = j
    #         if maze[i][j] == "G":
    #             gx = i
    #             gy = j

    # スタート地点をキューに入れ、その点の距離を0にする
    que = deque([])
    que.append((sx, sy))
    d[sx][sy] = 0

    # キューが空になるまでループ
    while que:
        # キューの先頭を取り出す
        p = que.popleft()
        # 取り出してきた状態がゴールなら探索をやめる
        # if p[0] == gx and p[1] == gy:
        #     break
        # 移動4方向をループ
        for i in range(4):
            # 移動した後の点を (nx, ny) とする
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            # 移動が可能かの判定とすでに訪れたことがあるかの判定
            # d[nx][ny] != INF なら訪れたことがある
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != "#" and d[nx][ny] == float("inf"):
                # 移動できるならキューに入れ、その点の距離を p からの距離 +1 で確定する
                que.append((nx, ny))
                d[nx][ny] = d[p[0]][p[1]] + 1

    return d



ans = 0
l = []
for h in range(H):
    for w in range(W):
        # ans = max(ans, bfs(w, h, w1, h1))
        # s = bfs(w, h)
        for s in bfs(h, w):
          # print(s)
          for j in s:
              if j != float("inf"):
                    l.append(j)
print(max(l))

# print(ans)
# print(bfs())      


