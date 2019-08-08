# TODO: Instead of completely removing the release year from the dataset, split the title column into <title> and <release_year>

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
    films.append(row['title'].replace(years[i], ''))
    i=i+1
    filmID.append(i)

for index, row in data.iterrows():
    gList = row['genres'].split('|')
    genres.append(gList)

newData = pd.DataFrame(list(zip(filmID, films, genres, years)))
newData.columns = ['ID','film','genre(s)','year']

newData.to_csv(r'dataset/movies_improved.csv', index=False)

print(newData.head(150).to_string())
