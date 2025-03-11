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