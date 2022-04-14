import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = "D:/Coding/Git/annenberg/data/tweet_data.csv"

tweet_data = pd.read_csv(FILE_PATH)

print(tweet_data.head(10))