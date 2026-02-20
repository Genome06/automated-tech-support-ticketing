import pandas as pd

class KnowledgeBase:
    def __init__(self, data_source):
        """
        data_source can be a local path (data/dataset.csv) or a raw URL from GitHub.
        """
        print(f"Loading Knowledge Base from {data_source}...")
        self.df = pd.read_csv(data_source)
        # We only keep unique intent-response pairs to avoid redundancy
        self.kb = self.df[['intent', 'response']].drop_duplicates(subset=['intent'])
        print("✅ Knowledge Base loaded!")

    def get_base_response(self, intent):
        # Looking for the response corresponding to the predicted intent
        result = self.kb[self.kb['intent'] == intent]['response']
        if not result.empty:
            return result.values[0]
        return "Sorry, no specific procedure found for this request."