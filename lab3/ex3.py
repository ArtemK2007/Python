sentence = input("Введіть речення: ")

words = sentence.split()

longest_word = max(words, key=len)

if len(longest_word) > 10:
    print("Твердження правдиве: найдовше слово має більше 10 символів.")
else:
    print("Твердження хибне: найдовше слово має 10 або менше символів.")
