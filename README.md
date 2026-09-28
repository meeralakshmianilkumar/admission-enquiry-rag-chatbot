# 🎓 Admission Enquiry RAG Chatbot

A Retrieval-Augmented Generation (RAG) based chatbot that answers
admission-related questions using official admission documents.

## 🎯 Objective

The chatbot provides reliable answers to questions related to:

- Courses
- Fees
- Eligibility
- Required Documents
- Admission Deadlines
- Admission Procedures

## 🧠 Technology Stack

- Python
- LangChain
- Sentence Transformers
- FAISS
- Streamlit
- Large Language Model (LLM)
- PyPDF

## 🏗️ System Architecture

User Question
      ↓
Query Processing
      ↓
Vector Search
      ↓
Relevant Admission Documents
      ↓
RAG Pipeline
      ↓
LLM
      ↓
Answer + Source

## 📁 Project Structure

```text
admission-enquiry-rag-chatbot/
│
├── app/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── src/
├── tests/
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
