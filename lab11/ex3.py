import nltk
from nltk.corpus import gutenberg, stopwords
from nltk.tokenize import word_tokenize
import string
import matplotlib.pyplot as plt
from collections import Counter

# --- завантаження ресурсів NLTK ---
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('gutenberg', quiet=True)
nltk.download('stopwords', quiet=True)

# --- 1. Завантаження тексту ---
text = gutenberg.raw('chesterton-thursday.txt')
tokens = word_tokenize(text)
words = [w.lower() for w in tokens]

# --- 2. ТОП-10 до очищення ---
freq_raw = Counter(words)
top10_raw = freq_raw.most_common(10)

print("\nТОП-10 слів ДО очищення:")
print(top10_raw)

plt.figure(figsize=(10,5))
plt.bar([w for w, c in top10_raw], [c for w, c in top10_raw])
plt.title("ТОП-10 слів до очищення")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.grid(axis='y', alpha=0.3)
plt.show()

# --- 3. Очищення тексту ---
stop_words = set(stopwords.words('english'))
punct = set(string.punctuation)

clean_words = [
    w for w in words
    if w.isalpha() and w not in stop_words
]

# --- 4. ТОП-10 після очищення ---
freq_clean = Counter(clean_words)
top10_clean = freq_clean.most_common(10)

print("\nТОП-10 слів ПІСЛЯ очищення:")
print(top10_clean)

plt.figure(figsize=(10,5))
plt.bar([w for w, c in top10_clean], [c for w, c in top10_clean])
plt.title("ТОП-10 слів після очищення")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.grid(axis='y', alpha=0.3)
plt.show()
