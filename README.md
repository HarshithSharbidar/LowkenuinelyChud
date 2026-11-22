# LowkenuinelyChud 🎪

A document-based Question Answering System built using Python and Streamlit.

The application allows users to upload documents and ask questions about their contents. It processes the document, extracts information, builds a knowledge base, and generates answers using keyword-based retrieval and rule-based logical inference.

## Features

- Supports TXT, PDF, and DOCX files
- Extracts and processes document text
- Splits text into sentences
- Builds a knowledge base from extracted information
- Retrieves relevant facts using keyword matching
- Identifies IF-THEN rules
- Performs logical inference to derive conclusions
- Handles questions that cannot be answered from the document
- Simple interactive web interface

## Technologies Used

- Python
- Streamlit
- PyPDF
- python-docx
- Pandas

## System Architecture

The system consists of the following modules:

1. Document Processor – Extracts text from uploaded documents and processes sentences.
2. Knowledge Base – Stores facts and retrieves relevant information.
3. Question Processor – Analyses the user's question and extracts keywords.
4. Reasoning Engine – Applies logical rules to derive conclusions.
5. Answer Generator – Generates responses based on retrieved facts and inference.
6. Streamlit Interface – Provides an interactive user interface.

## How to Run

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_LINK