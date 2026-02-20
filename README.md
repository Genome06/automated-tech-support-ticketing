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
- [ ] **Week 4: Backend Development ,UI, & Packaging**
    - Developing the Streamlit UI, building the API layer with FastAPI, and final documentation.

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

## 💡 Technical Highlights & Challenges

### 1. Hybrid Intelligence Pipeline
The system uses a two-step inference process. First, a fine-tuned **DistilBERT** model identifies the user's intent with high speed and low cost. Second, the **Gemini 2.5-flash** model generates a human-like response grounded in the retrieved knowledge base.

### 2. Implementation of Confidence Thresholding
To ensure reliability, I implemented a Softmax-based confidence gate. If the classifier's probability is below **0.8**, the system triggers a fallback mechanism where the LLM asks for clarification instead of providing a potentially wrong answer.

### 3. Modular & Scalable Architecture
Following best practices in Software Engineering, the project is structured using **Object-Oriented Programming (OOP)**. The backend (FastAPI) is decoupled from the frontend (Streamlit), allowing for independent scaling and easier maintenance.

### 4. Efficient Model Hosting
Due to GitHub's file size limitations, model weights are hosted on **Hugging Face Hub**, while the codebase remains lightweight and version-controlled on GitHub.
