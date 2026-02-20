import torch
import joblib
import torch.nn.functional as F
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer, DistilBertConfig
from src.utils import preprocess_text

class IntentClassifier:
    def __init__(self, model_path, tokenizer_path, le_path):
        self.tokenizer = DistilBertTokenizer.from_pretrained(tokenizer_path)
        config = DistilBertConfig.from_pretrained(tokenizer_path, num_labels=27)
        self.model = DistilBertForSequenceClassification(config)
        self.model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
        self.model.eval()
        self.le = joblib.load(le_path)

    def predict(self, text):
        clean_text = preprocess_text(text)
        inputs = self.tokenizer(clean_text, return_tensors="pt", truncation=True, padding=True, max_length=64)
        
        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = F.softmax(outputs.logits, dim=1)
            max_prob, intent_idx = torch.max(probs, dim=1)
            
        intent = self.le.inverse_transform([intent_idx.item()])[0]
        return intent, max_prob.item()