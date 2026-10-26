import os
import math

def clean_text_to_words(text):
    word = text.split()
    cleaned_words = [w.strip(".,!?\"'()[]:;").lower() for w in word]
    return cleaned_words


def compute_idf(all_chunks, global_vocab):
    """
    Compute the Inverse Document Frequency (IDF) for each word in the global vocabulary.
    IDF is calculated as log(N / df), where N is the total number of documents (chunks)
    and df is the number of documents containing the word.
    """
    N = len(all_chunks)
    idf_dict = {}

    vocab_set = set(global_vocab)
    for word in vocab_set:

        chunk_count = sum(1 for chunk in all_chunks if word in clean_text_to_words(chunk["text"]))
        if chunk_count == 0:
            chunk_count = 1  # To avoid division by zero
        idf_dict[word] = math.log(N / chunk_count) +1

    return idf_dict

def paragraph_to_tfidf_vector(paragraph, global_vocab, idf_dict):
    """
    Convert a paragraph into a TF-IDF vector based on the global vocabulary and IDF values.
    """
    words = clean_text_to_words(paragraph)
    vector = [0.0] * len(global_vocab)

    vocab_dict = {word: idx for idx, word in enumerate(global_vocab)}

    for word in words:
        if word in vocab_dict:
            index = vocab_dict[word]
            vector[index] += 1.0

    for word, index in vocab_dict.items():
        if vector[index] > 0:
            vector[index] = vector[index] * idf_dict.get(word, 1.0)

    return vector

def get_magnitude(vector):

    return math.sqrt(sum(x ** 2 for x in vector))

def cosine_similarity(vec1, vec2):
    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
    mag1 = get_magnitude(vec1)
    mag2 = get_magnitude(vec2)

    if mag1 * mag2 > 0:
        return dot_product / (mag1 * mag2)
    return 0.0

