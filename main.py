import os
from core.parser import stream_any_document
from core.vectorizer import clean_text_to_words, compute_idf, paragraph_to_tfidf_vector, cosine_similarity

def main():
    file_path = "datasets/test.docx"  # Replace with your document path

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    print("=" * 60)
    print(f"Streaming content from: {file_path}")
    print("=" * 60)

    print("\n[step 1/3] Building global vocabulary (setraming vectors)...")
    global_vocab_set = set()
    all_chunks = []

    try:
        for chunk, location in stream_any_document(file_path):
            words = clean_text_to_words(chunk)
            global_vocab_set.update(words)
            all_chunks.append({"text": chunk, "location": location})
    except Exception as e:
        print(f"Error while streaming document: {e}")
        return

    global_vocab = sorted(list(global_vocab_set))
    print(f"Global vocabulary size: {len(global_vocab)} words")

    idf_dict = compute_idf(all_chunks, global_vocab)
    if not all_chunks:
        print("⚠ No valid chunks found in the document.")
        return

    print("\n[step 2/3] Creating document matrix...")
    document_matrix = []

    for chunk in all_chunks:
        vec = paragraph_to_tfidf_vector(chunk["text"], global_vocab, idf_dict)
        document_matrix.append(vec)

    print(f"Document matrix created with {len(document_matrix)} chunks.")
    print("=" * 60)

    print("\n[step 3/3] Searching for a query...")
    print("(type 'exit' to quit the engine)")

    while True:
        query = input("\nEnter your search query: ").strip()
        if not query:
            continue
        if query.lower() == "exit":
            print("Exiting the search engine. Goodbye!")
            break

        query_vector = paragraph_to_tfidf_vector(query, global_vocab, idf_dict)
        best_match_idx = -1
        highest_score = -1.0

        for idx, doc_vector in enumerate(document_matrix):
            sim_score = cosine_similarity(query_vector, doc_vector)

            if sim_score > highest_score:
                highest_score = sim_score
                best_match_idx = idx

        if highest_score > 0.10:
            matched_chunk = all_chunks[best_match_idx]
            
            print(f"Location: {matched_chunk['location']} (similarity score: {highest_score:.4f})")
            print("-" * 50)
            print(matched_chunk["text"])
            print("-" * 50)
        else:
            print("No relevant matches found for your query.")

if __name__ == "__main__":
    main()