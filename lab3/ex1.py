text = input("Введіть текст: ")

if len(text) >= 21:
    result = text[:21:5]
    print("Результат зрізу:", result)
else:
    print("Текст занадто короткий для зрізу (потрібно хоча б 21 символ).")
