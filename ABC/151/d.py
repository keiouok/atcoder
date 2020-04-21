from collections import deque

H, W = map(int, input().split())
maze = [list(input()) for i in range(H)]
# print(maze)

# (sx, sy) から (gx, gy) への最短距離を求める
# 辿り着けないと INF
def bfs(sy, sx):
    # すべての点を INF で初期化
    d = [[float("inf")] * W for i in range(H)]

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
    que.append((sy, sx))
    d[sy][sx] = 0
    
    max_root = 0
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
            nx = p[1] + dx[i]
            ny = p[0] + dy[i]

            # 移動が可能かの判定とすでに訪れたことがあるかの判定
            # d[nx][ny] != INF なら訪れたことがある
            if 0 <= nx < W and 0 <= ny < H and maze[ny][nx] != "#" and d[ny][nx] == float("inf"):
                # 移動できるならキューに入れ、その点の距離を p からの距離 +1 で確定する
                que.append((ny, nx))
                d[ny][nx] = d[p[0]][p[1]] + 1
                max_root = max(max_root, d[ny][nx])    
    return max_root



ans = 0
for h in range(H):
    for w in range(W):
        if maze[h][w] == ".":
            ans = max(bfs(h, w), ans)
print(ans)

# print(ans)
# print(bfs())      


