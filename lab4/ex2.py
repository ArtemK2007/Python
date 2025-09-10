rows = 7
cols = 7
array = []

for i in range(rows):
    row = []
    for j in range(cols):
        if j % 2 == 0:
            row.append(1)
        else:
            row.append(0)
    array.append(row)

for row in array:
    print(row)