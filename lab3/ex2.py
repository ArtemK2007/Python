word = input("Введіть слово: ")

has_digits = any(ch.isdigit() for ch in word)

if has_digits:
    print("У слові є цифри.")
else:
    print("У слові немає цифр.")
