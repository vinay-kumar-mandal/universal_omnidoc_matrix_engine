import os
import math

def clean_text_to_words(text):

    word = text.split()

    cleaned_words = [w.strip(".,!?;:") for w in word]
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

    vocab = [0] * len(global_vocab)

    vocab_dict = {word: idx for idx, word in enumerate(global_vocab)}

    for word in words:
        if word in vocab_dict:
            index = vocab_dict[word]
            vector[index] += 1

    return vector

def get_magnitude(vector):

    return math.sqrt(sum(x ** 2 for x in vector))

def cosine_similarity(vec1, vec2):
    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))

    mag1 = get_magnitude(vec1)
    mag2 = get_magnitude(vec2)
    if mag1 *mag2 > 0:
        return dot_product / (mag1 * mag2)
    else:
        return 0

def create_document_matrix(all_paragraphs, global_vocab):
    matrix = []
    for paragraph in all_paragraphs:
        vector = paragraph_to_vector(paragraph, global_vocab)
        matrix.append(vector)

    return matrix
