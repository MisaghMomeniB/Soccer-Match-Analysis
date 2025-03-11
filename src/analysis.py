# Loading and Preprocessing the Data
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv("soccer_matches.csv")

# Display the first few rows and dataset info
print(df.head())
print(df.info())

# Encode team names to numeric values (Home and Away teams)
label_encoder = LabelEncoder()
df['home_team_encoded'] = label_encoder.fit_transform(df['home_team'])
df['away_team_encoded'] = label_encoder.fit_transform(df['away_team'])

# Calculate match result (1 = Home win, 0 = Draw, -1 = Away win)
df['result'] = df.apply(lambda row: 1 if row['home_goals'] > row['away_goals'] else (0 if row['home_goals'] == row['away_goals'] else -1), axis=1)

# Display the transformed data with encoded teams and match results
print(df[['home_team', 'away_team', 'home_team_encoded', 'away_team_encoded', 'result']].head())

# Exploratory Data Analysis (EDA)
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the plotting style
sns.set(style="whitegrid")

# Create subplots for visualizing different factors
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Boxplot for home team shots vs. match result
sns.boxplot(x='result', y='shots_home', data=df, ax=axes[0, 0])
sns.boxplot(x='result', y='shots_away', data=df, ax=axes[0, 1])
axes[0, 0].set_title('Home Team Shots vs. Match Result')
axes[0, 1].set_title('Away Team Shots vs. Match Result')

# Boxplot for possession percentage vs. match result
sns.boxplot(x='result', y='possession_home', data=df, ax=axes[1, 0])
sns.boxplot(x='result', y='possession_away', data=df, ax=axes[1, 1])
axes[1, 0].set_title('Home Team Possession vs. Match Result')
axes[1, 1].set_title('Away Team Possession vs. Match Result')

# Adjust the layout for better display
plt.tight_layout()
plt.show()

#  Preparing Data for Modeling

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Selecting features (X) and target (y)
X = df[['home_team_encoded', 'away_team_encoded', 'possession_home', 'possession_away', 'shots_home', 'shots_away', 'passes_home', 'passes_away']]
y = df['result']

# Splitting the data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardizing the feature data (important for many models)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model Building and Prediction

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Build a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)