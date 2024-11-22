def recommend_songs(song_index, top_n=3):
    similar_songs = list(enumerate(similarity_matrix[song_index]))
    
    # Sort by similarity score (descending order) and exclude the song itself
    sorted_songs = sorted(similar_songs, key=lambda x: x[1], reverse=True)[1:]
    
    recommendations = []
    for i in range(top_n):
        song_idx = sorted_songs[i][0]
        recommendations.append(df['Song_Name'][song_idx])
    
    return recommendations

# Recommend songs similar to "Song A"
song_index = 0  # "Song A" is at index 0
recommended_songs = recommend_songs(song_index)
print(f"Recommended songs for 'Song A': {recommended_songs}")
