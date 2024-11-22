# Feature matrix with 'Tempo', 'Energy', and 'Genre_Code'
features = df[['Tempo', 'Energy', 'Genre_Code']].values

# Normalize the data if needed (e.g., scaling to have mean 0 and variance 1)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Display the normalized feature matrix
print(features_scaled)
