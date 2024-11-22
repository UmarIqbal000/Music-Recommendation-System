# Convert categorical 'Genre' into numerical values
df['Genre_Code'] = df['Genre'].map({'Pop': 0, 'Rock': 1, 'Jazz': 2})

# Display updated dataframe
print(df)
