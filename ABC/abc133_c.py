l, r = map(int, input().split())
# 2019
if r - l >= 2019:
	print(0)
# 2019 以上なら良い
# この数の中に2019が含まれている．
# 2019 * 2019 - 2019 

else:
	ans = 10000
	for i in range(l, r + 1):
		for j in range(i + 1, r + 1):
			ans = min(ans, (i * j) % 2019)
	print(ans)
