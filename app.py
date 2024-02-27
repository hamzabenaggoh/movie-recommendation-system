import tensorflow as tf
print(tf.__version__)
import tensorflow_hub as hub
from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors



def create_app():
    app = Flask(__name__)

    model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

    def embed(text):
        return model(text)

    
    df = pd.read_csv("Top_10000_Movies.csv", engine="python")
    df = df[["original_title", "overview"]].dropna().reset_index(drop=True)
    df = df[:5500]
    titles = list(df["overview"])
    embeddings = embed(titles)


    @app.route('/recommend', methods=['GET'])
    def recommend():
        movieTitle = request.args.get('movie_title')
        Qembedding = embed([movieTitle])
        similar = cosine_similarity(Qembedding, embeddings)[0]
        topI = similar.argsort()[-3:][::-1]
        recommendations = df["original_title"].iloc[topI].tolist()
        return jsonify({"recommendations": recommendations})

    return app




if __name__ == "__main__":
    app = create_app()
    app.run(debug=False, port=8012)
