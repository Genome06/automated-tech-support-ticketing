from google import genai

class ResponseGenerator:
    def __init__(self, api_key, model_name='gemini-2.5-flash'):
        self.client = genai.Client(api_key=api_key)
        self.model_id = model_name

    def generate(self, query, intent, base_info, is_fallback=False):
        if is_fallback:
            prompt = f"The user said: '{query}'. Ask politely for clarification."
        else:
            prompt = f"""
            You are a professional tech support. Your name is TechBot. A user has made the following request:
            User Query: {query}
            Intent: {intent}
            Knowledge Base: {base_info}
            
            Task: Provide a helpful and polite response based on the Knowledge Base.
            """
            
        response = self.client.models.generate_content(
            model=self.model_id,
            contents=prompt
        )
        return response.text