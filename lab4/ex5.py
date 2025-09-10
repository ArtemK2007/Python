def most_frequent_digits(digits):
    count = {str(i): 0 for i in range(10)}
    for d in digits:
        if d in count:
            count[d] += 1

    max_count = max(count.values())

    most_frequent = [digit for digit, c in count.items() if c == max_count]

    return most_frequent, max_count


user_input = input("Введіть набір цифр: ")

digits, count = most_frequent_digits(user_input)

print(f"Цифри, які зустрічаються найчастіше ({count} разів): {', '.join(digits)}")
