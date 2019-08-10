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

newData.to_csv(r'dataset/movies_improved.csv', index=False)

print(newData.head(150).to_string())
