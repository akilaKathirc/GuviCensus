from docx import Document
import pandas as pd
import streamlit as st

def read_docx_to_dataframe(docx_path):
    # Load the docx file
    doc = Document(docx_path)
    
    # Create a list to hold the text
    doc_text = []
    
    # Iterate through each paragraph in the document
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():  # Only add non-empty paragraphs
            doc_text.append(paragraph.text)
    
    return doc_text
