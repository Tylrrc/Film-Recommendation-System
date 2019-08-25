import pandas as pd

data = pd.read_csv('dataset/movies.csv')

filmID = []
years = []
films = []
genres = []

for index, row in data.iterrows():
    years.append(row['title'][-6:])

i = 0
for index, row in data.iterrows():
    films.append(row['title'].replace(' ' + years[i], ''))
    filmID.append(row['movieId'])
    i = i + 1

for index, row in data.iterrows():
    gList = row['genres'].split('|')
    genres.append(gList)

newData = pd.DataFrame(list(zip(filmID, films, genres, years)))
newData.columns = ['movieId','title','genres','year']

newData = newData.sort_values(by=['title'])

newData.to_csv(r'dataset/movies_improved.csv', index=False)

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

df = pd.DataFrame(data=movies_avgRtg_genres[['movieId', 'title', 'rating', 'genres', 'tag_y']]).drop_duplicates(subset=['movieId'])

df.to_csv('dataset/MasterSet.csv')
