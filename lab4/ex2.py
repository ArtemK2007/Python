rows = 7
cols = 7

a = [[1 if j % 2 == 0 else 0 for j in range(cols)] for i in range(rows)]

for r in a:
    print(*r)
