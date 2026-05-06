import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import preprocess

class TFIDFChatbot:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

        
        self.df["clean_question"] = self.df["question"].apply(preprocess)

       
        self.vectorizer = TfidfVectorizer(ngram_range=(1,2))
        self.X = self.vectorizer.fit_transform(self.df["clean_question"])

    def get_response(self, query):
        query = preprocess(query)
        query_vec = self.vectorizer.transform([query])

        similarity = cosine_similarity(query_vec, self.X)

        max_score = similarity.max()
        index = similarity.argmax()

       
        if max_score < 0.3:
            return None, None, max_score

        matched_q = self.df.iloc[index]["question"]
        answer = self.df.iloc[index]["answer"]

        return matched_q, answer, max_score