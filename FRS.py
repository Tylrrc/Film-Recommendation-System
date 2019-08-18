# TODO: Mechanism to compare genre lists
# TODO: Need to fix TEST.csv output. Results missing: reason undetermined for now
# TODO: Redo earlier data manipulations. Use 'movieID' to group everything.
import warnings

import pandas as pd

warnings.filterwarnings('ignore')

movies = pd.read_csv("dataset/movies_improved.csv")

ratings = pd.read_csv("dataset/ratings.csv")

tags = pd.read_csv("dataset/tags.csv")

movie_ratings_combo = pd.merge(movies, ratings, on='movieId')

ratings_mean_count = pd.DataFrame(movie_ratings_combo.groupby('title')['rating'].mean())

MVAvg = pd.merge(ratings_mean_count, movie_ratings_combo, on='title')

movies_by_avg_rating = pd.DataFrame(MVAvg.groupby('title')['rating_y'].mean().sort_values(ascending=False))

movies_by_avg_rating["Genre Matches"] = ""

movies_avgRtg_genres = pd.merge(ratings_mean_count, movies, on='title')

movies_avgRtg_genres = pd.merge(movies_avgRtg_genres, tags, on=['movieId'], how='outer')

#print(movies_avgRtg_genres.to_string())

tag_lists = pd.DataFrame(movies_avgRtg_genres.groupby('title')['tag'].apply(list))

#del movies_avgRtg_genres['movieId']
del movies_avgRtg_genres['year']
del movies_avgRtg_genres['userId']
del movies_avgRtg_genres['timestamp']

movies_avgRtg_genres = pd.merge(movies_avgRtg_genres, tag_lists, on='title')

finalSet = movies_avgRtg_genres[['title', 'rating', 'genres', 'tag_y']]

#df = pd.DataFrame(data=movies_avgRtg_genres[['movieId', 'title', 'rating', 'genres', 'tag_y']]).drop_duplicates(subset=[])
#print(df.to_string())

# I D E A L  O U T P U T!!!!!!!!!!!!!!!!!!
#print(df.to_string())

MVAvg.to_csv('surewhynot.csv')

movies_avgRtg_genres.drop_duplicates(subset='movieId').to_csv(r'dataset/TEST.csv', index=False)

#ratings_mean_count['rating_counts'] = pd.DataFrame(movie_ratings_combo.groupby('title')['rating'].count())
#print(ratings_mean_count.to_string())
#user_movie_rating = movie_ratings_combo.pivot_table(index='userId', columns='title', values='rating')

#selection = input("Enter a film on which to base recommendations: ")

#selection_row = user_movie_rating[selection]

#print(selection_row.to_string()) #"selection_row"== Left column: Critic ID::::::Right column: Critic score
                                 # If a critic didn't vote on the movie, a value of NaN is seen as opposed to a score.
                                 # If a critic DID vote, then a 0.0-5.0 score is seen.

#print(ratings_mean_count.to_string())

#similar = user_movie_rating.corrwith(selection_row)

#corrFG = pd.DataFrame(similar, columns=['Correlation'])
#corrFG.dropna(inplace=True)

#corrFG = corrFG.join(ratings_mean_count['rating_counts'])

#print(corrFG[corrFG ['rating_counts']>50].sort_values('Correlation', ascending=False).head(25))
exit()


