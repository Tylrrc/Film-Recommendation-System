# TODO: Instead of completely removing the release year from the dataset, split the title column into <title> and <release_year>

import pandas as pd

data = pd.read_csv('dataset/movies.csv')

years = []
films = []
genres = []

for index, row in data.iterrows():
    years.append(row['title'][-6:])

i = 0
for index, row in data.iterrows():
    films.append(row['title'].replace(years[i], ''))
    i=i+1

for index, row in data.iterrows():
    gList = row['genres'].split('|')
    genres.append(gList)

newData = pd.DataFrame(list(zip(films, genres, years)))

newData.to_csv(r'dataset/movies_improved.csv')
