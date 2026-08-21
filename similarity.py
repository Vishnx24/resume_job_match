from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text,job_description_text):
    documents=[resume_text,job_description_text]
    vectorizer=TfidfVectorizer(stop_words="english")

    vector=vectorizer.fit_transform(documents)

    similarity=cosine_similarity(vector[0:1],vector[1:2])

    score=similarity[0][0]*100

    return round(score,2)
