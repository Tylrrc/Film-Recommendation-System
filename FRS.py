# TODO: Mechanism to compare genre lists

import warnings

import pandas as pd

warnings.filterwarnings('ignore')

movies = pd.read_csv("dataset/movies_improved.csv")

ratings = pd.read_csv("dataset/ratings.csv")

movie_ratings_combo = pd.merge(movies, ratings, on='movieId')

ratings_mean_count = pd.DataFrame(movie_ratings_combo.groupby('title')['rating'].mean())

#print(ratings_mean_count.to_string())

# TODO: Need to merge ratings_mean_count and movie_ratings_combo on 'title'

MVAvg = pd.merge(ratings_mean_count, movie_ratings_combo, on='title')

movies_by_avg_rating = pd.DataFrame(MVAvg.groupby('title')['rating_y'].mean().sort_values(ascending=False))

print(movies_by_avg_rating.to_string())

#print(MVAvg.head(20).to_string())

ratings_mean_count['rating_counts'] = pd.DataFrame(movie_ratings_combo.groupby('title')['rating'].count())

user_movie_rating = movie_ratings_combo.pivot_table(index='userId', columns='title', values='rating')

selection = input("Enter a film on which to base recommendations: ")

selection_row = user_movie_rating[selection]

#print(selection_row.to_string()) #"selection_row"== Left column: Critic ID::::::Right column: Critic score
                                 # If a critic didn't vote on the movie, a value of NaN is seen as opposed to a score.
                                 # If a critic DID vote, then a 0.0-5.0 score is seen.

similar = user_movie_rating.corrwith(selection_row)

corrFG = pd.DataFrame(similar, columns=['Correlation'])
corrFG.dropna(inplace=True)

corrFG = corrFG.join(ratings_mean_count['rating_counts'])

#print(corrFG[corrFG ['rating_counts']>50].sort_values('Correlation', ascending=False).head(25))


