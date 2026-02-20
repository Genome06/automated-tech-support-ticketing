import os
import sys
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.knowledge_base import KnowledgeBase
from dotenv import load_dotenv # add this line to import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Setup path agar bisa akses src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.classifier import IntentClassifier
from src.generator import ResponseGenerator

app = FastAPI(title="Tech-Support AI Backend")

# --- INITIALIZATION (Singleton Pattern) ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "..", "models")
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv")

# Component Initialization
classifier = IntentClassifier(
    model_path=os.path.join(MODELS_DIR, "best_model_state.bin"),
    tokenizer_path=os.path.join(MODELS_DIR, "tokenizer"),
    le_path=os.path.join(MODELS_DIR, "label_encoder.joblib")
)

generator = ResponseGenerator(api_key=os.getenv("GEMINI_API_KEY"))
knowledge_base = KnowledgeBase(data_source=DATA_PATH)

class ChatRequest(BaseModel):
    query: str

@app.post("/chat", responses={500: {"description": "Internal server error"}})
async def chat_endpoint(request: ChatRequest):
    try:
        # Intent Classification
        intent, confidence = classifier.predict(request.query)
        
        # Logic Threshold & Generation
        if confidence < 0.8:
            response = generator.generate(request.query, intent, None, is_fallback=True)
            return {"intent": "clarification_needed", "confidence": round(confidence, 4), "response": response}
        
        # Normal Flow
        base_info = knowledge_base.get_base_response(intent)
        response = generator.generate(request.query, intent, base_info)
        
        return {
            "intent": intent,
            "confidence": round(confidence, 4),
            "response": response
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))