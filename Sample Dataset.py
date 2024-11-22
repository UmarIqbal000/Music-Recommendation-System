import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample dataset of songs (each song has features like genre, tempo, energy)
data = {
    'Song_ID': [1, 2, 3, 4, 5],
    'Song_Name': ['Song A', 'Song B', 'Song C', 'Song D', 'Song E'],
    'Genre': ['Pop', 'Rock', 'Pop', 'Jazz', 'Pop'],
    'Tempo': [120, 140, 130, 90, 135],  # tempo in BPM
    'Energy': [0.7, 0.9, 0.6, 0.4, 0.8],  # energy from 0 to 1
}

df = pd.DataFrame(data)

# Display the dataset
print(df)
