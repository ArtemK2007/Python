def next_fibonacci_greater_than(p: int) -> int:
    a, b = 1, 1
    while b <= p:
        a, b = b, a + b
    return b
