from pulp import * # pip install pulp
n, r = len(kw), range(len(kw))
m = LpProblem(sense=LpMaximize) # 数理モデル
x = [[0 if kw[i][-1] != kw[j][0] else LpVariable('x%d_%d'%(i,j), cat=LpBinary)
      for j in r] for i in r] # kw_i から kw_j に繋げるかどうか (1)
y = [LpVariable('y%d'%i, lowBound=0) for i in r] # kw_iが先頭かどうか (2)
z = [LpVariable('z%d'%i, lowBound=0) for i in r] # kw_iの順番 (3)
m += lpSum(x[i][j] for i in r for j in r) # なるべく繋げる (0)
for i in r:
    cou = lpSum(x[i][j] for j in r) # kw_i から出る数
    cin = lpSum(x[j][i] for j in r) # kw_i へ入る数
    m += cou <= 1 # kw_i から出る数は1以下 (4)
    m += cin <= 1 # kw_i へ入る数は1以下 (5)
    m += cou <= cin + y[i] # yに関する制約 (6)
    for j in r:
        m += z[i] <= z[j]-1+(n+1)*(1-x[i][j]) # zに関する制約 (7)
m += lpSum(y) == 1 # 先頭は1つだけ (8)
# %time m.solve() # 求解
print(int(value(m.objective)) + 1) # 最長しりとり数
rr = range(1,n+1)
vx = np.vectorize(value)(x).astype(int)
i, s = 0, int(np.vectorize(value)(y)@rr)
while s:
    if i:
        print(' -> ', end='')
    i += 1
    print('[%d]%s'%(i,kw[s-1]), end=' ')
    s = vx[s-1]@rr
