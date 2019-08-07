# TODO: Instead of completely removing the release year from the dataset, split the title column into <title> and <release_year>

import pandas as pd

data = pd.read_csv('~/Downloads/ml-latest-small/movies.csv')

#data = pd.read_csv('~/Downloads/ml-20m/movies.csv')

data['title'] = data['title'].str.replace(r'[(\d4)]', '')

print(data.head(100).to_string())
