def most_frequent_digits(digits_set, user_input):
    count = {str(d): 0 for d in digits_set}

    for d in user_input:
        if d in count:
            count[d] += 1

    max_count = max(count.values())

    most_frequent = {digit for digit, c in count.items() if c == max_count}

    return most_frequent, max_count


digits_set = {0,1,2,3,4,5,6,7,8,9}

user_input = input("Введіть набір цифр: ")

most_freq_digits, count = most_frequent_digits(digits_set, user_input)

print(f"Цифри, які зустрічаються найчастіше ({count} разів): {', '.join(sorted(most_freq_digits))}")
