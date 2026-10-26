import os
import math

def clean_text_to_words(text):

    word = text.split()

    cleaned_words = [w.strip().lower() for w in word]
    return cleaned_words

def get_global_vocab(all_paragraphs):
    global_vocab = set()
    for paragraph in all_paragraphs:
        words = clean_text_to_words(paragraph)
        global_vocab.update(words)

    return sorted(global_vocab)


def paragraph_to_vector(paragraph, global_vocab):
    words = clean_text_to_words(paragraph)
    vector = [0] * len(global_vocab)

    for word in words:
        if word in global_vocab:
            index = global_vocab.index(word)
            vector[index] += 1

    return vector
