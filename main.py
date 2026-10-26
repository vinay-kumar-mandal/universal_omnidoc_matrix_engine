import os
from core.parser import stream_any_document
from core.vectorizer import clean_text_to_words, paragraph_to_vector, cosine_similarity

def main():
    file_path = "path/to/your/document.pdf"  # Replace with your document path

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
            words = clean_text_to_words(chunk_text)
            global_vocab_set.update(words)
            all_chunks.append({"text": chunk, "location": location})
    except Exception as e:
        print(f"Error while streaming document: {e}")
        return

    global_vocab = sorted(list(global_vocab_set))
    print(f"Global vocabulary size: {len(global_vocab)} words")

    if not all_chunks:
        print("⚠ No valid chunks found in the document.")
        return

    print("\n[step 2/3] Creating document matrix...")
    document_matrix = []

    for chunk in all_chunks:
        vec = paragraph_to_vector(chunk["text"], global_vocab)
        document_matrix.append(vec)

    print(f"Document matrix created with {len(document_matrix)} chunks.")
    print("=" * 60)
    