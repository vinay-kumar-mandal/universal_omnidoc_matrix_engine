import math
import os

from core.vectorizer import paragraph_to_vector, cosine_similarity

def search_query(query, global_vocab, document_matrix, all_paragraphs):
    query_vector = paragraph_to_vector(query, global_vocab)
    best_matches = -1
    highest_score = -1.0

    for index, doc_vector in enumerate(document_matrix):
        dot_product = sum(query_vector[i] * doc_vector[i] for i in range(len(global_vocab)))

        if dot_product > highest_score:
            highest_score = dot_product
            best_matches_index = index

    if highest_score > 0:
        return all_paragraphs[best_matches_index], highest_score
    else:
        return "No relevant matches found.", 0