# Retrieval-Augmented Generation (RAG) Model for QA Bot

## Overview
This project implements a Retrieval-Augmented Generation (RAG) model for a QA bot, combining retrieval and generative approaches to answer questions based on provided documents. The solution includes a Streamlit frontend for user interaction and uses Pinecone DB for efficient document retrieval and Cohere API for text generation.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Model Architecture](#model-architecture)
4. [Approach to Retrieval](#approach-to-retrieval)
5. [Generative Responses](#generative-responses)
6. [Modular and Scalable Code](#modular-and-scalable-code)
7. [Documentation and Approach](#documentation-and-approach)
8. [Additional Documentation](#additional-documentation)

## Installation

### Prerequisites
- Python 3.9 or later
- Docker (for containerization)

### Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/repository.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd repository
   ```
3. **Create and Activate a Virtual Environment (optional but recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\Scripts\activate
   ```
4. **Install the Required Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Streamlit App Locally:**
   ```bash
   streamlit run app.py
   ```

6. **Build and Run Docker Container (optional):**
   ```bash
   docker build -t rag-qa-bot .
   docker run -p 8501:8501 rag-qa-bot
   ```
   Access the app at `http://localhost:8501`.

## Usage

1. **Start the Streamlit App:**
   ```bash
   streamlit run app.py
   ```
2. **Access the Application:**
   Open a web browser and go to `http://localhost:8501`.

3. **Upload Documents:**
   Use the file uploader in the Streamlit interface to upload PDF documents.

4. **Ask Questions:**
   Enter your queries in the text box and submit to get answers based on the uploaded documents.

## Model Architecture

- **Document Storage and Retrieval:** Uses Pinecone DB for storing and retrieving document embeddings.
- **Generative Model:** Utilizes Cohere API for generating responses based on the context retrieved from documents.

## Approach to Retrieval

- **Data Preparation:** Text is extracted from PDFs and split into manageable sections.
- **Embedding and Storage:** Text sections are embedded using Cohere API and stored in Pinecone DB with metadata.
- **Query Processing:** User queries are embedded and used to retrieve relevant document sections from Pinecone DB.

## Generative Responses

- **Context Compilation:** Aggregates relevant sections of text to provide context for answering questions.
- **Generation:** Generates responses using the Cohere API based on the provided context.

## Modular and Scalable Code

- **Frontend:** Built with Streamlit for a responsive and interactive user interface. Code is modular with reusable components.
- **Backend:** Handles document processing, embedding generation, and service interactions. Code is organized into functions for maintainability and scalability.

## Documentation and Approach

- **Decisions Made:**
  - **Model Selection:** Chose Cohere API for its advanced text generation capabilities and Pinecone DB for efficient vector storage.
  - **Text Handling:** Split text into sections to enhance retrieval accuracy and manage large documents effectively.
- **Challenges Faced:**
  - **Large Document Handling:** Implemented text splitting and optimized embedding storage.
  - **Service Integration:** Ensured seamless interaction between Pinecone DB, Cohere API, and Streamlit frontend.
- **Solutions Implemented:**
  - **Efficient Storage:** Used Pinecone DB for scalable storage and retrieval.
  - **Modular Code:** Ensured clear separation of functionality for easy maintenance and scalability.
  
## Additional Documentation

- [Colab Notebook](https://github.com/viveklearning/Bot_to_answer_from_pdfs/blob/main/db.ipynb) - Demonstrates the entire pipeline from data loading to question answering.
- [Deployment Videos](https://github.com/viveklearning/Bot_to_answer_from_pdfs/blob/main/assignment_sample3_2.mp4) - Provides visual explanations of the deployment process.
