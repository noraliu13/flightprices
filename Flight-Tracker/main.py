import pandas as pd

data = pd.read_csv('Clean_Dataset.csv')
data.airline.value_counts()