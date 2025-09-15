N = int(input("Enter N: "))
if 1 <= N <= 9:
    for i in range(N, 0, -1):
        print("  " * (i - 1), end="")
        for j in range(i, N + 1):
            print(j, end=" ")
        print()
else:
    print("N must be between 1 and 9")
