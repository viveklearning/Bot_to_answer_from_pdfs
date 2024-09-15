# %% Install dependencies
# !pip install pinecone-client cohere streamlit PyPDF2

import streamlit as st
from PyPDF2 import PdfReader
import cohere
import pinecone

# Initialize Cohere and Pinecone clients
co = cohere.Client('brV6x6dombNlECLz3031MhwM2UxHom1Gx2mp0BX8')
pc = pinecone.Pinecone(api_key='564a623c-4d0a-4247-8f53-1e171c26b4e2')
index_name = "quickstart2"
index = pc.Index(index_name)

# Load PDF file and extract text
def load_pdf(pdf_file):
    pdf = PdfReader(pdf_file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""
    return text

# Get embeddings for the text using Cohere
def get_embeddings(text):
    response = co.embed(texts=[text])
    return response.embeddings[0]

# Store document embeddings in Pinecone
def store_embeddings_in_sections(document_id, document_text, section_size=150):
    words = document_text.split()
    sections = [' '.join(words[i:i+section_size]) for i in range(0, len(words), section_size)]
    
    for idx, section in enumerate(sections):
        section_id = f"{document_id}_section_{idx+1}"
        section_embedding = get_embeddings(section)
        index.upsert([(section_id, section_embedding, {'text': section})])

# Retrieve the most relevant document sections from Pinecone
def retrieve_documents(query_embedding):
    results = index.query(vector=query_embedding, top_k=3, include_values=True, include_metadata=True)
    return results['matches']

# Generate an answer using Cohere's generative model
def generate_answer(question, context):
    response = co.generate(prompt=f"Question: {question}\nContext: {context}\nAnswer:", max_tokens=200)
    return response.generations[0].text

# Streamlit app
st.title("RAG-based QA Bot")
st.write("Upload a PDF document and ask questions based on its content.")

# Upload PDF
uploaded_pdf = st.file_uploader("Upload a PDF file", type="pdf")
if uploaded_pdf:
    document_text = load_pdf(uploaded_pdf)
    st.write("Document loaded successfully!")

    # Store document embeddings in Pinecone
    store_embeddings_in_sections("uploaded_document", document_text)
    st.write("Document stored in the vector database.")

# Ask a question
question = st.text_input("Ask a question about the document")
if question:
    query_embedding = get_embeddings(question)
    retrieved_segments = retrieve_documents(query_embedding)
    
    # Extract relevant context from retrieved document segments
    context = "\n\n".join([segment['metadata'].get('text', '') for segment in retrieved_segments])
    
    # Generate and display the answer
    answer = generate_answer(question, context)
    st.header('Answer')
    st.write(answer)

    # Display the context
    st.header('Relevant Segments')
    st.write(context)
