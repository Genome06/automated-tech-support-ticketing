# Automated Tech-Support Ticketing System

An end-to-end automated customer support ticketing management system powered by Deep Learning and Large Language Models (LLMs). This project aims to automate incoming ticket classification and generate initial response drafts to enhance customer service efficiency.

## 🚀 Key Features
- **Automated Classification**: Classifies customer tickets into 11 major categories using Transformers architecture (BERT/DistilBERT) implemented in PyTorch.
- **AI-Powered Response Generation**: Integrates LLMs to generate automated, professional response drafts based on the identified ticket category and intent.
- **Interactive Dashboard**: Visualizes ticket statistics and trends using Tableau for data-driven insights.
- **User Interface**: Features an interactive demo built with Streamlit for real-time ticket submission simulations.

## 🛠️ Tech Stack
- **Programming Language**: Python
- **Deep Learning**: PyTorch, Hugging Face Transformers
- **API Framework**: FastAPI
- **Frontend/UI**: Streamlit
- **Data Visualization**: Tableau, Pandas
- **Version Control**: Git & GitHub

## 📊 Dataset
This project utilizes the **Bitext Customer Support Training Dataset**, containing ~27,000 rows of interactions across 11 categories (Account, Order, Refund, etc.) and 27 specific intents.

## 🛣️ Project Milestones
- [X] **Week 1: Data Preparation & PyTorch Environment**
    - Environment setup, Exploratory Data Analysis (EDA), and building Custom Dataset/DataLoader classes.
- [X] **Week 2: Training Classifier (The Deep Learning Part)**
    - Fine-tuning BERT/DistilBERT models for multi-class text classification.
- [X] **Week 3: LLM Integration**
    - LLM integration for auto-responses.
- [ ] **Week 4: Backend Development ,UI, Dashboard, & Packaging**
    - Developing the Streamlit UI, building the API layer with FastAPI, creating the Tableau Dashboard, and final documentation.

## 📂 Repository Structure
```text
├── data/               # Raw and processed datasets
├── notebooks/          # Google Colab notebooks for experimentation
├── models/             # Trained model weights (.pth files) 
├── src/                # Main Python scripts (preprocessing, training)
├── app/                # Streamlit & FastAPI application code
└── README.md           # Project documentation
└── requirements.txt    # Library List
```

*Note: Due to file size limits, model weights are hosted on [Hugging Face](https://huggingface.co/genome06/automated_tech_support_ticketing_model).*
