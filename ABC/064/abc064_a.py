r, g, b = map(int, input().split())
c = 100 * r + 10 * g + b
if c % 4 == 0:
    print("YES")
else:
    print("NO")
