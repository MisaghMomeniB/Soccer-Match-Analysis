# Loading and Preprocessing the Data
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv("soccer_matches.csv")

# Display the first few rows and dataset info
print(df.head())
print(df.info())