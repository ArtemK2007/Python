from fibonaci import next_fibonacci_greater_than

def main():
    p = int(input("Введіть число p: "))
    result = next_fibonacci_greater_than(p)
    print(f"Перше число Фібоначчі більше за {p} це: {result}")

if __name__ == "__main__":
    main()
