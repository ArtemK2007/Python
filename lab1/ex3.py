N = int(input("Enter N: "))
if 1 <= N <= 9:
    for i in range(1, N):
        for j in range(i, N):
            print(j, end=" ")
        print()
else:
    print("N must be between 1 and 9")