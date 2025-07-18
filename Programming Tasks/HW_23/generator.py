import random

def load_words_from_file(filename='words.txt'):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def readable_word_generator(count: int, filename='words.txt'):
    if count > 10_000:
        raise ValueError("Max count is 10,000")

    word_list = load_words_from_file(filename)

    if count > len(word_list):
        raise ValueError(f"Requested {count} words, but only {len(word_list)} available.")

    selected_words = random.sample(word_list, count)
    for word in selected_words:
        yield word
