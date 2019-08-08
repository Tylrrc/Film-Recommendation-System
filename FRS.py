import warnings

import pandas as pd

warnings.filterwarnings('ignore')

movies = pd.read_csv("dataset/movies.csv")

ratings = pd.read_csv("dataset/ratings.csv")

movie_ratings_combo = pd.merge(movies, ratings, on='movieId')

ratings_mean_count = pd.DataFrame(movie_ratings_combo.groupby('title')['rating'].mean())

ratings_mean_count['rating_counts'] = pd.DataFrame(movie_ratings_combo.groupby('title')['rating'].count())

UMR = movie_ratings_combo.pivot_table(index='userId', columns='title', values='rating')

selection = input("Enter a film on which to base recommendations: ")

selection_row = UMR[selection]

similar = UMR.corrwith(selection_row)

corrFG = pd.DataFrame(similar, columns=['Correlation'])
corrFG.dropna(inplace=True)

corrFG = corrFG.join(ratings_mean_count['rating_counts'])

print(corrFG[corrFG ['rating_counts']>50].sort_values('Correlation', ascending=False).head(25))


