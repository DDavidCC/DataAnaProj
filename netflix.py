import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the Netflix dataset

netflix_df = pd.read_csv('/Users/s3int/Downloads/workspace/netflix_data.csv')

print(netflix_df)

netflix_subset =  netflix_df[netflix_df["type"] == "Movie"]

subset = netflix_subset[netflix_subset["release_year"] >= 1990]

movies_1990s = subset[subset["release_year"] < 2000]

plt.hist(movies_1990s)
plt.title('Distribution of Movies Released in the 1990s')
plt.xlabel('Release Year')
plt.ylabel('Number of Movies')
plt.show()

Action_movies = movies_1990s[movies_1990s["Genre"] == " Action"]

duration = 90
short_action_movies = 0

for label, row in Action_movies.iterrows():
    if row["duration"] < duration:
        short_action_movies += 1
    else:
        short_action_movies += 0

print("Short Action Movie Count: {short_action_movies}")

plt.hist(movies_1990s)
plt.title('Distribution of Movies Released in the 1990s')
plt.xlabel('Release Year')
plt.ylabel('Number of Movies')
plt.show()
