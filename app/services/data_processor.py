from langchain.text_splitter import RecursiveCharacterTextSplitter

def process_uploaded_file(filepath: str):
    """Extract and chunk text."""
    # Very basic text reading (expand later for PDF/DOCX)
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_text(text)
    return chunks
