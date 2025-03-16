 # Conversational AI Text Processing Pipeline

 ## Overview

  Welcome to Conversational AI Text Processing Pipeline (CHAT SCRIBE), a powerful and modular NLP application built using LangGraph. This project provides an end-to-end solution for analyzing text input through three key stages:
  
  Text Classification – Categorizes input text into predefined categories such as News, Blog, Research, or Other.
  
  Entity Extraction – Identifies and extracts key entities such as persons, organizations, and locations.
  
  Text Summarization – Generates a concise summary of the provided text.
  
  This workflow demonstrates the power of LangGraph in building structured, extensible, and efficient NLP applications. By the end of this tutorial, you'll have a deep understanding of how to construct a graph-based NLP pipeline that can be customized or expanded for 
  various use cases.

# 🛠  Features


  ✅ Automated Text Classification – Classifies input text into meaningful categories.
  
  ✅ Entity Recognition – Extracts organizations, people, and locations from text.
  
  ✅ Smart Summarization – Generates concise and informative summaries.
  
  ✅ Modular Architecture – Built with LangGraph, making it scalable and customizable.
  
  ✅ Conversational UI – Integrated with Streamlit for an intuitive user experience.
  
  ✅ Document Download API – Users can download analysis results in a structured document format.

# 🔧  How It Works

    1️⃣ User Input: The user submits a text query.
    
    2️⃣ API Processing: The system processes the input through the following steps:

    ## Text Classification – Assigns a relevant category.
    
    Entity Extraction – Identifies key entities.
    
    Summarization – Generates a concise summary.
    3️⃣ Output Generation: The system returns results in a structured format.
    
    4️⃣ Download Feature: Users can download the processed output as a document.

# 📌  API Endpoint

    The system interacts with the following API endpoint:
    
    Endpoint: http://127.0.0.1:8000/process_text

# 📥 Installation & Setup

    git clone : https://github.com/TahaDataAlchemy/GenAI-agents.git
    
    python -m venv venv
    
    venv\Scripts\activate
    
    pip install -r requirements.txt
    
    streamlit run app.py
    
    uvicorn main:app --reload


  

![image](https://github.com/user-attachments/assets/98894240-0aee-4502-88a4-7a4b15e44417)

![image](https://github.com/user-attachments/assets/0dd5a760-50f8-4a2f-b4a7-8d7da99c0023)

