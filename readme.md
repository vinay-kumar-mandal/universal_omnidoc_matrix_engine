# OmniDoc Matrix Engine

A lightweight, memory-efficient Document Search Engine built from scratch using pure mathematics and Python. It processes multiple document formats on a sentence level and uses Vector Space Modeling for text retrieval.

## Features
- **Universal Streaming Parser:** Lazy-loads content from PDF, DOCX, PPTX, and XLSX formats without loading the entire file into RAM, preventing memory crashes.
- **Mathematical Core:** Implements custom TF-IDF (Term Frequency-Inverse Document Frequency) vectorization without external machine learning libraries.
- **Vector Space Matching:** Uses Cosine Similarity to analyze structural angles between query vectors and document chunk spaces.
- **Granular Chunking:** Automatically splits large paragraphs into optimized sentence-level arrays to preserve vector balance and boost search precision.

## Project Structure
```text
omnidoc_matrix_engine/
│
├── core/
│   ├── __init__.py
│   ├── parser.py         # File streaming logic & chunking handlers
│   └── vectorizer.py     # Math functions (TF-IDF & Cosine Similarity)
│
├── datasets/             # Directory to place input files
│   └── test.docx
│
├── main.py               # Main execution and query loop
└── README.md
```

## Setup & Installation

1. Clone or navigate to your project root folder:
   ```bash
   cd omnidoc_matrix_engine
   ```

2. Activate your virtual environment (if applicable) and install the lightweight document dependencies:
   ```bash
   pip install pypdf python-docx python-pptx openpyxl
   ```

## Usage

1. Place your target document (PDF, DOCX, PPTX, or XLSX) inside the `datasets/` directory.
2. Open `main.py` and set your configuration path:
   ```python
   file_path = "datasets/your_file.pdf"
   ```
3. Run the search engine from your terminal:
   ```bash
   python main.py
   ```
4. Enter your technical or structural search phrases into the prompt. Type `exit` to close the engine.
