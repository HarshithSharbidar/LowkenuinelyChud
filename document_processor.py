import re
from pypdf import PdfReader
from docx import Document


def clean_text(text):

    # Replace multiple spaces and line breaks with single spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def extract_text(uploaded_file):

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".txt"):

        text = uploaded_file.getvalue().decode("utf-8")

    elif file_name.endswith(".pdf"):

        reader = PdfReader(uploaded_file)
        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + " "

    elif file_name.endswith(".docx"):

        document = Document(uploaded_file)

        text = " ".join(
            paragraph.text
            for paragraph in document.paragraphs
        )

    else:

        raise ValueError("Unsupported file format.")
    
    cleaned_text = clean_text(text)
    print("CLEANED PDF TEXT:", repr(cleaned_text[:2000]))
    return cleaned_text


def split_into_sentences(text):

    # Separate numbered list items
    text = re.sub(r'\s+(?=\d+\.\s)', '\n', text)

    # Separate bullet points
    text = re.sub(r'\s+●\s*', '\n', text)

    sentences = re.split(
        r'(?<=[.!?])\s+',
        text
    )

    return [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]